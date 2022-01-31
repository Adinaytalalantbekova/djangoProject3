from django.urls import path
from . import views
from .forms import LoginForm

app_name = "users"
urlpatterns = [
    path("register/", views.Registration.as_view(), name="registration"),
    path("login/", views.NewLoginView.as_view(), tamplate_name="login.html",
                                                 authentication_form=LoginForm),
    path("users/", views.UserListView.as_view(), name="user_list"),
]