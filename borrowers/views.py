from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from borrowers import forms


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = 'auth/login.html'
    success_url = '/home/'

    def form_valid(self, form):
        credentials = form.cleaned_data
        print(credentials)
        user = authenticate(
            username=credentials['email'],
            password=credentials['password'],
        )

        print(user)

        if user is None or user.is_staff:
            messages.error(self.request, 'Invalid Credentials')
            return super(LoginView, self).form_invalid(form)

        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
