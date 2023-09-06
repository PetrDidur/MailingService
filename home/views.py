from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from blog.models import Blog
from home.services import get_cached_clients
from mailing.models.mailing import Mailing
from mailing.models.client import Client


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['mailing'] = Mailing.objects.all()
            context['client'] = Client.objects.all()
        context['client'] = get_cached_clients(user=self.request.user)
        context['mailing'] = Mailing.objects.filter(user=self.request.user)

        all_blogs = Blog.objects.all()
        random_blogs = sample(list(all_blogs), 3)

        context['blog'] = random_blogs
        return context


class GuestPageView(TemplateView):
    template_name = 'home_guest.html'
