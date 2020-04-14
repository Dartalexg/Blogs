from django.forms import ModelForm
from .models import Commets
class CommentForm(ModelForm):
    class Meta:
        "Форма коментов"
        model=Commets
        fields=('text',)