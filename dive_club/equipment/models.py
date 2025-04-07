from django.db import models
from pages.validators import validate_image_file_size, validate_file_extension


class EquipmentCategory(models.Model):
    """Категория оборудования."""
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория оборудования"
        verbose_name_plural = "Категории оборудования"


class Equipment(models.Model):
    """Модель ремонтируемого оборудования."""
    name = models.CharField(max_length=100, verbose_name="Название оборудования")
    description = models.TextField(verbose_name="Краткое описание", blank=True, null=True)
    image = models.ImageField(
        upload_to='equipment/',
        validators=[validate_image_file_size, validate_file_extension],
        verbose_name="Изображение"
    )
    category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    detailed_description = models.TextField(
        verbose_name="Подробное описание ремонта",
        blank=True,
        null=True,
        help_text="Подробная информация о ремонтных работах и услугах"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ремонт оборудования"
        verbose_name_plural = "Ремонт оборудования"


class EquipmentPageContent(models.Model):
    """Контент страницы ремонта оборудования."""
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок страницы",
        default="Ремонт оборудования"
    )
    description = models.TextField(
        verbose_name="Вступительный текст страницы",
        blank=True,
        null=True
    )
    background_photo = models.ImageField(
        upload_to='equipment_page/',
        blank=True,
        null=True,
        verbose_name="Фоновое изображение",
        validators=[validate_image_file_size, validate_file_extension]
    )
    equipment = models.ManyToManyField(
        Equipment,
        related_name="equipment_page",
        blank=True,
        verbose_name="Список ремонтируемого оборудования"
    )

    def __str__(self):
        return "Контент страницы ремонта оборудования"

    class Meta:
        verbose_name = "Контент страницы ремонта оборудования"
        verbose_name_plural = "Контент страницы ремонта оборудования"
