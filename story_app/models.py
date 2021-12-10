from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class story_teller(models.Model):
    caption=models.CharField(max_length=50)
    storyteller=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.URLField()
    desc=models.TextField()

