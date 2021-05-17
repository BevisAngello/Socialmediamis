from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from SocialMediaThreats.models import Threats
from SocialMediaThreats.models import Techniques
from SocialMediaThreats.models import Awareness

class ThreatForm(forms.ModelForm):
    class Meta:
        model = Threats
        fields = "__all__"
        

class TechniquesForm(forms.ModelForm):
    class Meta:
        model = Techniques
        fields = "__all__"

class AwarenessForm(forms.ModelForm):
    class Meta:
        model = Awareness
        fields = "__all__" 

class CreateUserForm(UserCreationForm):
    username = forms.Field(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.Field(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
