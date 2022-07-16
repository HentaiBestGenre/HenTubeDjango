from django import forms
from .models import Video

class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=32)
    video = forms.FileField()
    preview = forms.ImageField()

class AddCommentForm(forms.Form):
    value = forms.CharField(max_length=32)
    video_id = forms.IntegerField()
    user_id = forms.IntegerField()

# в форме надо уточнять место запяси файла, в вьюшке нужно уточнять откуда его брать
# лучшить поисковую систему на диске, при большом колличестве видео и привью скорость поиска бует замедлена,
# разбить edia папку на разеделы с видео и т.д.