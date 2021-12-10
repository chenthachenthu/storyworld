from .models import story_teller
from django import forms
class Storyforms(forms.ModelForm):
    class Meta:
        model=story_teller
        fields=['caption','storyteller','desc']