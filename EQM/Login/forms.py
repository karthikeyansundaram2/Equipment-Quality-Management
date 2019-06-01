from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Login,Register


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('Role', 'LoginId','password',)
