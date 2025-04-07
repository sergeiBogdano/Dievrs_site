from django.db import models


class TrainingPage(models.Model):
    """Страница обучения"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание страницы")
    advantages = models.TextField(verbose_name="Преимущества обучения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница обучения"
        verbose_name_plural = "Страницы обучения"


class TrainingCourse(models.Model):
    """Курс обучения с категориями."""
    CATEGORY_CHOICES = [
        ('regular', 'Обычные курсы'),
        ('sdi_specialization', 'Специализации SDI'),
        ('first_response', 'Курсы первой медицинской помощи'),
    ]
    training_page = models.ForeignKey(
        TrainingPage,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Страница обучения"
    )
    title = models.CharField(max_length=255, verbose_name="Название курса")
    course_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='regular',
        verbose_name="Тип курса"
    )
    description = models.TextField(verbose_name="Описание курса")
    included = models.TextField(verbose_name="Что входит в курс")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс обучения"
        verbose_name_plural = "Курсы обучения"


class TrainingImage(models.Model):
    """Изображения, связанные с курсами обучения."""
    course = models.ForeignKey(
        TrainingCourse,
        on_delete=models.CASCADE,
        related_name="images",
        null=True,
        verbose_name="Курс"
    )
    image = models.ImageField(
        upload_to="training_images/",
        verbose_name="Изображение курса"
    )

    def __str__(self):
        return f"Изображение для {self.course.title}"

    class Meta:
        verbose_name = "Изображение курса"
        verbose_name_plural = "Изображения курсов"


class TrainingVideo(models.Model):
    """Видео для курсов обучения."""
    course = models.ForeignKey(
        TrainingCourse,
        on_delete=models.CASCADE,
        related_name="videos",
        verbose_name="Курс"
    )
    video = models.FileField(
        upload_to="training_videos/",
        verbose_name="Видео курса"
    )

    def __str__(self):
        return f"Видео для {self.course.title}"

    class Meta:
        verbose_name = "Видео курса"
        verbose_name_plural = "Видео курсов"
