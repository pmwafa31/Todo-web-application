from django.forms import ModelForm
from .models import Todo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1' ,'password2']