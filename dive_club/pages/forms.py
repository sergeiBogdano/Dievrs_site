from django import forms
from .models import HomePageContent, ContactPage, Application

class HomePageContentForm(forms.ModelForm):
    """Форма для редактирования контента главной страницы."""

    class Meta:
        model = HomePageContent
        fields = '__all__'
        widgets = {
            'big_text': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
                'style': 'width: 100%;'
            }),
            'small_text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 80,
                'style': 'width: 100%;'
            }),
            'discount_description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 80,
                'style': 'width: 100%;'
            }),
            'event_text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 80,
                'style': 'width: 100%;'
            }),
        }

class ContactPageForm(forms.ModelForm):
    """Форма для редактирования контактной информации."""

    class Meta:
        model = ContactPage
        fields = ['address', 'phone_numbers', 'email', 'social_links']


class ApplicationForm(forms.ModelForm):
    """Форма для подачи заявки."""

    class Meta:
        model = Application
        fields = ['name', 'email', 'message']
