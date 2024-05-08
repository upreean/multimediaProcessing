from django import forms

class AudioForm(forms.Form):
    videoFile = forms.FileField()