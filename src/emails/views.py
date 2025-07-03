from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import services
def verify_email_token_view(request, token, *args, **kwargs):
    did_verify, msg = services.verify_token(token)
    if not did_verify:
        return HttpResponse(msg)
    return HttpResponse(token)