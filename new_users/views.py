from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView

class Registration(CreateView):
    form_class = RegistrationForm
    success_url = '/users/'
    template_name = 'registration_user.html'


class NewLoginView(LoginView):
    form_class = LoginView
    template_name = 'login_user.html'

    def get_success_url(self):
        return reverse("users:user_list")


class UserListview(ListView):
    queryset = User.objects.all()
    template_name = "list_user.html"

    def get_queryset(self):
        return User.objects.all()
