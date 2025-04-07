from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    """Галерея изображений."""
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'images': images})
