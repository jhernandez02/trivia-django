from django.db import models
from django.conf import settings
from trivias.models import Trivia
from questions.models import Question

class Participation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.trivia.name}"

class Answer(models.Model):
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey('questions.Option', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participation} - {self.question.text}"
