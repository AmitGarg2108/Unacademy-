from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    class_level = models.CharField(max_length=10, blank=True, null=True)
    duration = models.IntegerField(default=20)  # duration in minutes

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField(choices=[(1,'Option 1'), (2,'Option 2'), (3,'Option 3'), (4,'Option 4')])

    def __str__(self):
        return self.question_text
