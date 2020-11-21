from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    email = forms.EmailField(required =True,max_length=256,help_text='youremail@gmail.com')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50,required=True)
    name = forms.CharField(max_length=50,required=True)
    form_email = forms.EmailField(max_length=50,required=True)
    message = forms.CharField(max_length=500,widget=forms.Textarea(),help_text='Write your message here')
