from django.db import models

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    class_name = models.CharField(max_length=100, blank=True)
    entrance_exam = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='study_materials/')

    def __str__(self):
        return self.title
