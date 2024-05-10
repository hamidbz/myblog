from django import forms


class Mesage(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    message = forms.Textarea()