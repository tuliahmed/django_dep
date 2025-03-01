from django import forms
from myapp.models import UserMoreInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserMoreInfoForm(forms.ModelForm):
    SocialMediaLink=forms.URLField(widget=forms.TextInput(attrs={'Placeholder':'Facebook Link '}))
    class Meta:
        model = UserMoreInfo
        fields = ('SocialMediaLink', 'Profile_Picture')