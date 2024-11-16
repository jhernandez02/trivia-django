from rest_framework import viewsets
from .models import Participation
from .serializers import ParticipationSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Participation, Answer
from questions.models import Question, Option
from django.db.models import Sum

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer

    @action(detail=True, methods=['post'])
    def submit_answers(self, request, pk=None):
        participation = self.get_object()
        answers_data = request.data.get('answers', [])
        score = 0

        for answer_data in answers_data:
            question_id = answer_data.get('question_id')
            option_id = answer_data.get('option_id')

            try:
                question = Question.objects.get(id=question_id)
                selected_option = Option.objects.get(id=option_id)

                if selected_option.is_correct:
                    score += question.points

                Answer.objects.create(
                    participation=participation,
                    question=question,
                    selected_option=selected_option
                )
            except (Question.DoesNotExist, Option.DoesNotExist):
                return Response(
                    {'error': f'Invalid question or option ID: {question_id}, {option_id}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        participation.score = score
        participation.save()

        return Response({'score': score}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def ranking(self, request):
        trivia_id = request.query_params.get('trivia_id')
        if not trivia_id:
            return Response({'error': 'Trivia ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        rankings = Participation.objects.filter(trivia_id=trivia_id)\
            .values('user__username')\
            .annotate(total_score=Sum('score'))\
            .order_by('-total_score')

        return Response(rankings, status=status.HTTP_200_OK)