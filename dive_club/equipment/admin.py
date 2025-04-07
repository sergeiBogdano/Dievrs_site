from django.contrib import admin
from .models import Equipment, EquipmentCategory, EquipmentPageContent
from .forms import EquipmentPageContentForm


@admin.register(EquipmentPageContent)
class EquipmentPageContentAdmin(admin.ModelAdmin):
    """Админский интерфейс для контента страницы ремонта оборудования."""
    form = EquipmentPageContentForm
    filter_horizontal = ('equipment',)
    fieldsets = (
        ('Основной контент', {'fields': ('title', 'description', 'background_photo')}),
        ('Оборудование', {'fields': ('equipment',)}),
    )


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    """Админский интерфейс для категорий ремонта оборудования."""
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """Админский интерфейс для ремонта оборудования."""
    list_display = ('name', 'category',)
    search_fields = ('name',)
    list_filter = ('category',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'image', 'category', 'detailed_description')}),
    )
