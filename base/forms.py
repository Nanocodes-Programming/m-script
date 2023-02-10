from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    sender = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, label='message', widget=forms.TextInput(attrs={'placeholder': 'message'}))