from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from pages.models import HomePageContent
from events.models import EventImage


def event_create(request):
    """Создание мероприятия."""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        images = request.FILES.getlist('images')
        homepage_content = HomePageContent.objects.first()
        event = Event.objects.create(title=title, description=description)
        event.homepage_content.add(homepage_content)

        EventImage.objects.bulk_create([
            EventImage(event=event, image=image) for image in images
        ])

        return redirect('home')
    return render(request, 'events/event_create.html')


def event_detail(request, event_id):
    """Детальная страница мероприятия."""
    event = get_object_or_404(Event, id=event_id)
    images = [img.image.url for img in event.images.all()]
    context = {
        'event': event,
        'images': images,
    }
    return render(request, 'events/event_detail.html', context)