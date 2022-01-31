from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models


ADMIN = 1
DOCTOR = 2
SINGER = 3
ACTOR = 4
COMEDIAN = 5
DANCER = 6
USER_TYPE =(
    (ADMIN, 'ADMIN'),
    (DOCTOR, 'DOCTOR'),
    (SINGER, 'SINGER'),
    (ACTOR, 'ACTOR'),
    (COMEDIAN, 'COMEDIAN'),
    (DANCER, 'DANCER')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, "FEMALE"),
    (OTHER, 'OTHER')
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = models.NewUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'hello'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder': 'password',
            'id': 'hi',
        }
    ))
