from django.contrib import admin
from .models import HomePageContent, AboutPage, ContactPage, TermsOfService, PrivacyPolicy, Certificate, Instructor, Application
from .forms import HomePageContentForm
from events.models import Event


class BaseAdmin(admin.ModelAdmin):
    """Базовый класс для админки с общими настройками."""
    search_fields = ('title',)
    ordering = ('-updated_at',)
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "validity")
    search_fields = ("title",)


class EventInline(admin.TabularInline):
    """Inline для мероприятий на главной странице."""
    model = Event.homepage_content.through
    extra = 1
    verbose_name = "Мероприятие"
    verbose_name_plural = "Мероприятия"


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    """Админский интерфейс для инструкторов."""
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'bio', 'avatar', 'room_photo')}),
    )


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    """Админский интерфейс для контента главной страницы."""
    form = HomePageContentForm
    inlines = [EventInline]
    filter_horizontal = ('certificates',)
    fieldsets = (
        ('Видео', {'fields': ('welcome_video', 'overlay_video_text')}),
        ('Фон и текст', {'fields': ('background_photo', 'big_text',
                                    'small_photo', 'small_text')}),
        ('Инструктор', {'fields': ('instructor',)}),
        ('Сертификаты', {'fields': ('certificates',)}),
        ('Скидки', {
            'fields': ('discount_title', 'discount_description',
                       'original_price', 'discounted_price',
                       'discount_percentage', 'discount_validity')
        }),
        ('Описание мероприятий', {'fields': ('event_text',)}),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    """Админский интерфейс для страницы 'О нас'."""
    fieldsets = (
        (None, {'fields': ('title', 'introduction', 'team_description', 'team_image',
                           'instructors', 'team_photo', 'mission_statement',
                           'mission_photo', 'mission_image', 'services',
                           'services_image', 'contact_info', 'social_links')}),
    )
    list_display = ('title',)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    """Админский интерфейс для страницы контактов."""
    list_display = ('address', 'email',)
    search_fields = ('email',)
    list_filter = ('address',)
    fieldsets = (
        ("Основная информация", {"fields": ("address", "phone_numbers", "email")}),
        ("Дополнительно", {"fields": ("map_link", "social_links")}),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """Админский интерфейс для заявок."""
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    fieldsets = (
        ("Контактные данные", {"fields": ("name", "email", "message")}),
        ("Системная информация", {"fields": ("created_at",)}),
    )
    readonly_fields = ("created_at",)


@admin.register(TermsOfService)
class TermsOfServiceAdmin(BaseAdmin):
    """Админский интерфейс для правил пользования."""
    list_display = ("title",)
    search_fields = ("title", "content")


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(BaseAdmin):
    """Админский интерфейс для политики конфиденциальности."""
    list_display = ("title",)
    search_fields = ("title", "content")
