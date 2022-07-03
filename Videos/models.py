from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    """ Table that contains videos data """

    title = models.CharField(max_length=32)
    pub_data = models.DateTimeField("date published", default=timezone.now())
    path_name = models.FileField(upload_to='Videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4'])
    ])
    creater = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    views = models.IntegerField(default=0)
    num_of_likes = models.IntegerField(default=0)
    num_of_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"""
        title: {self.title},
        publication date: {self.pub_data},
        creater id and name: {self.creater_id} \t {self.creater.username},
        views: {self.views},
        likes: {self.num_of_likes},
        dislikes: {self.num_of_dislikes},
        """


class Like(models.Model):
    """ Table that contains info about likes and users how put them """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    value = models.BooleanField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"""
        User: {self.user.username},
        Video: {self.video.title},
        value: {self.value}
        """


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    value = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"""
        User: {self.user.username},
        Video: {self.video.title},
        creation date: {self.date}
        """