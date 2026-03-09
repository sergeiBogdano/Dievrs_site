from django import forms
from .models import Equipment, EquipmentPageContent


class EquipmentForm(forms.ModelForm):
    """Форма для редактирования оборудования."""

    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 80,
                'style': 'width: 100%;'
            }),
        }


class EquipmentPageContentForm(forms.ModelForm):
    """Форма для редактирования контента страницы оборудования."""

    class Meta:
        model = EquipmentPageContent
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'width: 100%;'
            }),
            'description': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
                'style': 'width: 100%;'
            }),
        }
