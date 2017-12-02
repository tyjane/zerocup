from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()
    introduction = forms.CharField()

class MemoryForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    content = forms.CharField()
