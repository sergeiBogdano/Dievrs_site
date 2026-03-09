from django import forms
from .models import GalleryImage


class GalleryImageForm(forms.ModelForm):
    """Форма для загрузки изображений в галерею."""

    images = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = GalleryImage
        fields = []

    def save(self, commit=True):
        # Здесь мы не вызываем super().save(), т.к. создаём объекты напрямую
        images = self.files.getlist('images')
        for image in images:
            GalleryImage.objects.create(image=image)
        return None
