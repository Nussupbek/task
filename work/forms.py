from .models import Artiсles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NullBooleanSelect

class ArticlesForm(ModelForm):
    class Meta:
        model = Artiсles
        fields = ['title', 'description', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Загаловаок задачи'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дедлайн'
            })
        }