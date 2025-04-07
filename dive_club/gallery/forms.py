from django import forms
from .models import GalleryImage


class GalleryImageForm(forms.ModelForm):
    """Форма для загрузки изображений в галерею."""

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = GalleryImage
        fields = ['images']

    def save(self, commit=True):
        images = self.files.getlist('images')
        for image in images:
            GalleryImage.objects.create(image=image)
        return super().save(commit=False)
