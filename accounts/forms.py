from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name'] # contre Injection SQL
        user.last_name = self.cleaned_data['last_name'] # contre Injection SQL
        email = self.cleaned_data['email'] # contre Injection SQL

        if commit:
            user.save()

        return user

'''
form qui herite de UserChangeForm pour edit les info du user
'''
class EditProfileForm(UserChangeForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput,required=True)

    class Meta:
        model = User
        fields = [
        'email',
        'first_name',
        'last_name',
        'password',
        ]
