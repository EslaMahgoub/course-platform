from django.shortcuts import render
from django.conf import settings

from emails.models import Email
from emails.forms import EmailForm

EMAIL_ADDRESS = settings.EMAIL_ADDRESS
def home_view(request, *args, **kwargs):
    print(request.POST.get('email'))
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        'message': ''
        }
    if form.is_valid():
        email_value = form.cleaned_data.get('email')
        obj = form.save()
        email_obj, created = Email.objects.get_or_create(email=email_value)
        print(obj)
        context['form'] = EmailForm()
        context['message'] = f'Success! Check your email for verification from {EMAIL_ADDRESS}'
    else:
        print(form.errors)
    return render(request, 'home.html', context)