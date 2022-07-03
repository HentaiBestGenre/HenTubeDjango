from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=32)
    video = forms.FileField()