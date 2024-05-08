from django.db import models

class AudioModel (models.Model):
    videoFile = models.FileField(default="")
    audioFile = models.FileField()