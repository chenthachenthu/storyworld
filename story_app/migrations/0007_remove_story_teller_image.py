# Generated by Django 2.2 on 2021-12-07 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story_app', '0006_auto_20211207_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story_teller',
            name='image',
        ),
    ]