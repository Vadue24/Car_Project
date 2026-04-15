from .models import Car
from django.forms import ModelForm, TextInput, FileInput, Textarea, DateTimeInput, NumberInput


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'anons', 'price', 'full_text', 'date', 'picture']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control border-white bg-dark text-light'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control border-white bg-dark text-light'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control border-white bg-dark text-light'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control border-white bg-dark text-light',
                'rows': 6
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control border-white bg-dark text-light',
                'type': 'datetime-local'
            }),
            'picture': FileInput(attrs={
                'class': 'form-control border-white bg-dark text-light',
                'required': 'required',
            }),
        }
