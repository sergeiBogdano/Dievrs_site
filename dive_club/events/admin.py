from django.contrib import admin
from .models import Event, EventImage


class BaseAdmin(admin.ModelAdmin):
    """Базовый класс для админки с общими настройками."""
    search_fields = ('title',)
    ordering = ('-updated_at',)
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True


class EventImageInline(admin.TabularInline):
    """Inline для изображений мероприятий."""
    model = EventImage
    extra = 1


@admin.register(Event)
class EventAdmin(BaseAdmin):
    """Админский интерфейс для мероприятий."""
    inlines = [EventImageInline]
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')