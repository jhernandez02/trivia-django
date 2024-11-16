from rest_framework import viewsets
from .models import Trivia
from .serializers import TriviaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Trivia, TriviaAssignment

class TriviaViewSet(viewsets.ModelViewSet):
    queryset = Trivia.objects.all()
    serializer_class = TriviaSerializer

    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk=None):
        trivia = self.get_object()
        user_ids = request.data.get('user_ids', [])

        if not user_ids:
            return Response({"error": "No user IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        users = CustomUser.objects.filter(id__in=user_ids)
        if not users.exists():
            return Response({"error": "Invalid user IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Crear asignaciones
        assignments = []
        for user in users:
            assignment, created = TriviaAssignment.objects.get_or_create(trivia=trivia, user=user)
            if created:
                assignments.append(assignment)

        return Response(
            {"message": f"{len(assignments)} users assigned to trivia '{trivia.name}'."},
            status=status.HTTP_200_OK
        )
