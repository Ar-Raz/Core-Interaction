from django import forms
from django.conf import settings
from allauth.account.forms import SignupForm, PasswordField

ACCOUNT_CHOICES = (
    ("A","تایید"),
    ("B", "رد سفارش ")
)

class ConfirmForm(forms.Form):
    confirm_options = forms.ChoiceField(widget=forms.RadioSelect(),choices=ACCOUNT_CHOICES)


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='نام')
    last_name = forms.CharField(max_length=30, label='نام خانوادگی')
    username = forms.CharField(max_length=30, label ="نام کاربری")
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user