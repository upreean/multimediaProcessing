from django import forms

class ImageForm(forms.Form):
    imageFile = forms.ImageField()