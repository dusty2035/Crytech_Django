from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class Form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"hero__profile-information-box-profilesetting-settings-1" ,
            }
    ))


class Edit_profile_form(UserChangeForm):

    class Meta :
        model = User
        # use when want to add fields from User model
        fields = (
            'username',
            'email',
        )
        # use when want to remove fields from User model
        # exclude = ()
