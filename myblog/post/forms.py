from django import forms


class AddComentForm(forms.Form):
    writerNAme = forms.CharField(max_length=20)
    writerEmail = forms.EmailField(max_length=20)
    message = forms.CharField(max_length=1000)
    