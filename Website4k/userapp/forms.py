from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phonenumber = forms.IntegerField()
    address = forms.CharField(max_length=500)
    pincode = forms.IntegerField()





    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )