from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Medio'),
        ('hard', 'Difícil'),
    ]
    
    text = models.TextField()
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
