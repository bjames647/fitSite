from __future__ import absolute_import
from django.views import generic
from website.forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy



class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('profile')
    template_name = 'accounts/signup.html'


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

class UserPageView(generic.FormView):
    model = User
    template_name = 'accounts/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

