from django.contrib import admin
from .models import GalleryImage
from .forms import GalleryImageForm


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Админский интерфейс для галереи изображений."""
    form = GalleryImageForm
    list_display = ('id', 'uploaded_at')
    ordering = ('-uploaded_at',)
