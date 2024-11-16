from django.db import models
from django.conf import settings
from questions.models import Question

class Trivia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

class TriviaAssignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trivia_assignments')
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='assignments')    

    def __str__(self):
        return f"{self.user.username} -> {self.trivia.name}"