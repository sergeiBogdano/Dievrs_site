from django.shortcuts import render, get_object_or_404
from .models import TrainingPage, TrainingCourse


def training(request):
    """Страница обучения с курсами, изображениями и видео."""
    training_page = TrainingPage.objects.prefetch_related(
        "courses__images",
        "courses__videos"
    ).first()

    # ✅ Получаем курсы отсортированные по категории
    courses = TrainingCourse.objects.filter(
        training_page=training_page
    ).order_by('course_category')

    # ✅ Передаем choices из модели (названия категорий)
    category_choices = TrainingCourse.CATEGORY_CHOICES

    return render(request, "training/training.html", {
        "training": training_page,
        "courses": courses,
        "category_choices": category_choices,  # ← НОВОЕ!
    })


def course_detail(request, course_id):
    course = get_object_or_404(TrainingCourse, id=course_id)
    return render(request, "training/course_detail.html", {"course": course})