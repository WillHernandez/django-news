from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
        # eg below will only include age but not email
        # fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
        # eg below will only include the default form settings
        # fields = UserChangeForm.Meta.fields