# Generated by Django 2.2 on 2021-12-07 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story_app', '0003_remove_story_teller_storyteller'),
    ]

    operations = [
        migrations.AddField(
            model_name='story_teller',
            name='storyteller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]