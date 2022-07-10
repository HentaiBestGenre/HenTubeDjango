from django import forms

class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=32)
    video = forms.FileField()

class AddCommentForm(forms.Form):
    value = forms.CharField(max_length=32)
    video_id = forms.IntegerField()
    user_id = forms.IntegerField()