from rest_framework import serializers
from .models import Trivia
from questions.serializers import QuestionSerializer

class TriviaSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Trivia
        fields = ['id', 'name', 'description', 'questions']
