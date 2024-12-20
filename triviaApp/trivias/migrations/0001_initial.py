# Generated by Django 5.1.3 on 2024-11-16 17:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('questions', models.ManyToManyField(to='questions.question')),
            ],
        ),
        migrations.CreateModel(
            name='TriviaAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trivia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='trivias.trivia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trivia_assignments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
