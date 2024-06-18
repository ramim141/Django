from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView, CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm

class HomeView(TemplateView):
    template_name = 'home.html'

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Logged in successfully!')
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password.')
            return self.form_invalid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged out successfully!')
        return super().get(request, *args, **kwargs)

class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Password changed successfully!')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
