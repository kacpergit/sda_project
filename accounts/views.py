from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SubmittableAuthenticationForm, SignUpForm


class SubmittableLoginView(LoginView):
    title = 'Login'
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class SuccessMessegedLogoutView(LogoutView):

    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'You are now logged out!')
        return result


class SignUpView(CreateView):

    title = 'Sign Up'
    template_name = 'form.html'
    form_class = SignUpForm
    success_message = 'You successfully Signed Up!.'
    success_url = reverse_lazy('index')
