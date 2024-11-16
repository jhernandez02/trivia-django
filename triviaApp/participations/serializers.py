from rest_framework import serializers
from .models import Participation, Answer
from questions.serializers import QuestionSerializer, OptionSerializer

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    selected_option = OptionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'selected_option']

class ParticipationSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Participation
        fields = ['id', 'user', 'trivia', 'score', 'answers']
