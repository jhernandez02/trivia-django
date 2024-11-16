from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from questions.views import QuestionViewSet
from trivias.views import TriviaViewSet
from participations.views import ParticipationViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="TalaTrivia API",
        default_version='v1',
        description="API para gestionar trivias, preguntas y participaciones",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@talatrivia.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='question')
router.register('trivias', TriviaViewSet, basename='trivia')
router.register('participations', ParticipationViewSet, basename='participation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]