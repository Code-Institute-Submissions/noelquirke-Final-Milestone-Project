from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Email


class CreateEmailView(SuccessMessageMixin, CreateView):
    model = Email
    context_object_name = 'email'
    fields = ['email', 'name', 'phone', 'subject', 'message']
    success_message = 'Thank you, your message has been sent'

    def get_form(self, form_class=None):
        """Adds custom placeholders and widgets to form"""
        form = super().get_form(form_class)
        form.fields['email'].widget.attrs = {'placeholder': 'Email Address'}
        form.fields['name'].widget.attrs = {'placeholder': 'Full Name'}
        form.fields['phone'].widget.attrs = {'placeholder': 'Phone Number'}
        form.fields['subject'].widget.attrs = {'placeholder': 'Appointment Date/Time'}
        form.fields['message'].widget.attrs = {
            'placeholder': 'Any further information required?*'}
        form.fields['message'].label = ''
        return form

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Details necessary for Stripe payment processing
        contact_active = True

        context['contact_active'] = contact_active
        return context
