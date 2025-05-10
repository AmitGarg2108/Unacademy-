from django.db import models

class VideoLecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    entrance_exam = models.CharField(max_length=100, blank=True)
    video = models.FileField(upload_to='video_lectures/')

    def __str__(self):
        return self.title
