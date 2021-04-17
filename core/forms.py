from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    message = forms.CharField(max_length=500)
