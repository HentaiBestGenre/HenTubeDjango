from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=32)
    video = forms.FileField()

class AddComment(forms.Form):
    value = forms.CharField(max_length=32)
    video = forms.IntegerField()
    user = forms.IntegerField()