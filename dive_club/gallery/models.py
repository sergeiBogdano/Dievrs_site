from django.utils import timezone

from django.db import models
from pages.validators import validate_image_file_size, validate_file_extension


class GalleryImage(models.Model):
    """Фотогалерея."""
    image = models.ImageField(
        upload_to="gallery/",
        validators=[validate_image_file_size, validate_file_extension]
    )
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return f"Фото {self.id} ({self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"
