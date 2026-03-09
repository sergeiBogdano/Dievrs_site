from django.contrib import admin
from .models import TrainingCourse, TrainingPage, TrainingImage, TrainingVideo


class TrainingCourseInline(admin.TabularInline):
    """Inline для курсов обучения на странице TrainingPage."""
    model = TrainingCourse
    extra = 1
    verbose_name = "Курс"
    verbose_name_plural = "Курсы"
    fields = ('title', 'course_category')


@admin.register(TrainingPage)
class TrainingPageAdmin(admin.ModelAdmin):
    """Админский интерфейс для страницы обучения."""
    list_display = ("title",)
    inlines = [TrainingCourseInline]
    fieldsets = (
        ("Основное", {"fields": ("title", "description", "advantages")}),
    )


class TrainingImageInline(admin.TabularInline):
    """Inline для изображений, связанных с курсом обучения."""
    model = TrainingImage
    extra = 1


class TrainingVideoInline(admin.TabularInline):
    """Inline для видео, связанных с курсом обучения."""
    model = TrainingVideo
    extra = 1


@admin.register(TrainingCourse)
class TrainingCourseAdmin(admin.ModelAdmin):
    """Админский интерфейс для курсов обучения."""
    list_display = ('title', 'course_category')
    inlines = [TrainingImageInline, TrainingVideoInline]
    fieldsets = (
        (None, {'fields': ('training_page', 'title', 'course_category', 'description', 'included')}),
    )
