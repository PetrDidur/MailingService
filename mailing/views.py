from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from mailing.forms.client import ClientForm
from mailing.forms.mailing import MailingForm, ManagerMailingForm
from mailing.models.mailing_log import MailingLog
from mailing.models.client import Client
from mailing.models.mailing import Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('mailing.view_mailing'):
            return Mailing.objects.all()
        queryset = Mailing.objects.filter(user=self.request.user, is_active=True)
        return queryset


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('home:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')
    permission_required = 'mailing.can_change_mailing_is_active'

    def get_form_class(self):
        if self.request.user.is_staff or self.request.user.has_perm(self.permission_required):
            return ManagerMailingForm
        return MailingForm

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        queryset = Client.objects.filter(user=self.request.user)
        return queryset


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('home:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home:index')


class MailingLogListView(LoginRequiredMixin, ListView):
    model = MailingLog

    def get_queryset(self):
        if self.request.user.is_staff:
            return MailingLog.objects.all()
        queryset = MailingLog.objects.filter(mailing__user=self.request.user)
        return queryset
