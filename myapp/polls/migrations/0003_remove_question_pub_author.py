# Generated by Django 5.0.2 on 2025-03-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_pub_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_author',
        ),
    ]
