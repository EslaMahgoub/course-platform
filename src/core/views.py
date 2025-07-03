from django.shortcuts import render
from django.conf import settings

from emails.models import Email, EmailVerificationEvent
from emails.forms import EmailForm
from emails import services as email_services

EMAIL_ADDRESS = settings.EMAIL_ADDRESS

def home_view(request, *args, **kwargs):
    print(request.POST.get('email'))
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        'message': ''
        }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = email_services.start_verification_event(email_val)
        print(obj)
        context['form'] = EmailForm()
        context['message'] = f'Success! Check your email for verification from {EMAIL_ADDRESS}'
    else:
        print(form.errors)
    return render(request, 'home.html', context)