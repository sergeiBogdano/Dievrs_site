from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from .validators import validate_image_file_size, validate_file_extension, validate_video_file_size


class Certificate(models.Model):
    """Сертификат для дайв-клуба."""
    image = models.ImageField(
        upload_to='certificates/',
        verbose_name="Изображение сертификата",
        validators=[validate_image_file_size, validate_file_extension]
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название сертификата"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание сертификата"
    )
    validity = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Срок действия сертификата"
    )
    terms = models.TextField(
        blank=True,
        null=True,
        verbose_name="Условия использования сертификата"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"


class Instructor(models.Model):
    """Модель инструктора."""
    name = models.CharField(max_length=100, verbose_name="Имя инструктора")
    bio = models.TextField(verbose_name="Биография инструктора")
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Аватар инструктора"
    )
    room_photo = models.ImageField(
        upload_to='instructors/',
        blank=True,
        null=True,
        verbose_name="Помещение"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"


class HomePageContent(models.Model):
    """Контент главной страницы."""
    welcome_video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True,
        verbose_name="Видео приветствия",
        validators=[validate_video_file_size, validate_file_extension]
    )
    background_photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name="Большое изображение",
        validators=[validate_image_file_size, validate_file_extension]
    )
    big_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Большой текст (на первой фотографии)"
    )
    small_photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name="Малое изображение",
        validators=[validate_image_file_size, validate_file_extension]
    )
    small_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Малый текст"
    )
    overlay_video_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Текст на видео"
    )
    instructor = models.ForeignKey(
        "Instructor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Инструктор"
    )
    certificates = models.ManyToManyField(
        Certificate,
        blank=True,
        verbose_name="Сертификаты"
    )
    event_text = models.CharField(
        max_length=100,
        verbose_name="Описание мероприятий",
        blank=True,
        null=True
    )
    discount_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название скидки"
    )
    discount_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание скидки"
    )
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Цена без скидки"
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Цена со скидкой"
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Процент скидки",
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # Исправлено
    )
    discount_validity = models.DateField(
        blank=True,
        null=True,
        verbose_name="Срок действия скидки"
    )

    def __str__(self):
        return "Контент главной страницы"

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"


class AboutPage(models.Model):
    """Страница 'О нас'."""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    introduction = models.TextField(verbose_name="Введение")
    team_description = models.TextField(verbose_name="Описание команды", blank=True, null=True)
    team_image = models.ImageField(
        upload_to='about/team/',
        verbose_name="Изображение команды",
        blank=True,
        null=True
    )
    instructors = models.ManyToManyField(Instructor, blank=True, verbose_name="Инструкторы")
    team_photo = models.ImageField(
        upload_to='about/team/',
        blank=True,
        null=True,
        verbose_name="Фото команды",
        validators=[validate_image_file_size, validate_file_extension]
    )
    mission_statement = models.TextField(verbose_name="Наша миссия")
    mission_photo = models.ImageField(
        upload_to='about/mission/',
        blank=True,
        null=True,
        verbose_name="Фото миссии",
        validators=[validate_image_file_size, validate_file_extension]
    )
    mission_image = models.ImageField(
        upload_to='about/mission_image/',
        blank=True,
        null=True,
        verbose_name="Изображение миссии",
        validators=[validate_image_file_size, validate_file_extension]
    )
    services = models.TextField(verbose_name="Наши услуги")
    services_image = models.ImageField(
        upload_to='about/services_image/',
        blank=True,
        null=True,
        verbose_name="Изображение услуг",
        validators=[validate_image_file_size, validate_file_extension]
    )
    contact_info = models.TextField(verbose_name="Связь с нами")
    social_links = models.JSONField(verbose_name="Ссылки на соцсети", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class ContactPage(models.Model):
    """Страница контактов."""
    address = models.CharField("Адрес", max_length=255)
    phone_numbers = models.JSONField("Телефонные номера", default=list)
    email = models.EmailField("Электронная почта")
    map_link = models.URLField("Ссылка на карту")
    social_links = models.JSONField("Социальные сети", default=dict)

    class Meta:
        verbose_name = "Контактная страница"
        verbose_name_plural = "Контактные страницы"

    def __str__(self):
        return "Контактная информация"


class TermsOfService(models.Model):
    """Правила пользования."""
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Правила пользования"
        verbose_name_plural = "Правила пользования"

    def __str__(self):
        return "Правила пользования"


class PrivacyPolicy(models.Model):
    """Политика конфиденциальности."""
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Политика конфиденциальности"
        verbose_name_plural = "Политика конфиденциальности"

    def __str__(self):
        return "Политика конфиденциальности"


class Application(models.Model):
    """Модель заявки."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка от {self.name}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
