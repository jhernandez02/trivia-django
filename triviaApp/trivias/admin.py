from django.contrib import admin

# Register your models here.
from .models import Trivia, TriviaAssignment

admin.site.register(Trivia)
admin.site.register(TriviaAssignment)
