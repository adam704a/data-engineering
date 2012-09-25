from django import forms

class UploadOrderForm(forms.Form):
    myFile = forms.FileField()