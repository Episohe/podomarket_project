from allauth.account.views import PasswordChangeView
from django.shortcuts import render

from django.urls import reverse


def index(request):
    return render(request, 'podomarket/index.html')


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
