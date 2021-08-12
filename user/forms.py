from django import forms
# from django.forms import Form
from .models import *
import datetime


class ContactUsForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	subject = forms.CharField(max_length=255)
	message = forms.CharField(required=False,
							   widget=forms.Textarea)



# login&signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = "__all__"
		exclude = ['user']






