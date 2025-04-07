from pages.models import HomePageContent
from pages.validators import validate_image_file_size, validate_file_extension

from django.db import models
from django.utils import timezone


class Event(models.Model):
    """Модель мероприятия."""
    title = models.CharField(max_length=100, verbose_name="Название мероприятия")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(
        verbose_name="Описание мероприятия",
        blank=True,
        null=True
    )
    homepage_content = models.ManyToManyField(
        HomePageContent,
        related_name='events',
        verbose_name="Контент главной страницы",
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class EventImage(models.Model):
    """Изображения для мероприятия."""
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='events/',
        validators=[validate_image_file_size, validate_file_extension]
    )

    def __str__(self):
        return f"{self.event.title} - Image"
