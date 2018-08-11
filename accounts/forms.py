from django import forms

class HomeForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()
