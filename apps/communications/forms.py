from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=254)
