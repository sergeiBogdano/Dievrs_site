from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm

def gallery(request):
    """Галерея изображений с возможностью загрузки нескольких файлов."""
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # сохранение нескольких изображений
            return redirect('gallery')  # редирект после успешной загрузки
    else:
        form = GalleryImageForm()

    images = GalleryImage.objects.all().order_by('-uploaded_at')
    context = {
        'images': images,
        'form': form
    }
    return render(request, 'gallery/gallery.html', context)
