from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Name of Article"
            }),
            "anons": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Anons of Article"
            }),
            "data": DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "Date of publish"
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Text of Article"
            })
        }