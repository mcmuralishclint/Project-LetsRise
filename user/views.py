# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard:index')
    template_name = 'registration/signup.html'