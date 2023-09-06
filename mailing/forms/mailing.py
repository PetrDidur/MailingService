from django import forms

from mailing.models.mailing import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['title', 'body', 'mailing_time', 'frequency', 'clients']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'mailing_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
        }


class ManagerMailingForm(MailingForm):
    class Meta:
        model = Mailing
        fields = ['is_active']
        widgets = {
            'is_active': forms.CheckboxInput(),
        }
