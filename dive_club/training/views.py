from django.shortcuts import render, get_object_or_404
from .models import TrainingPage, TrainingCourse


def training(request):
    """Страница обучения с курсами, изображениями и видео."""
    training_page = TrainingPage.objects.prefetch_related("courses__images", "courses__videos").first()

    # Получаем уникальные категории курсов
    categories = TrainingCourse.objects.values_list("course_category", flat=True).distinct()

    return render(request, "training/training.html", {
        "training": training_page,
        "categories": categories  # Передаем в шаблон
    })


def course_detail(request, course_id):
    course = get_object_or_404(TrainingCourse, id=course_id)
    return render(request, "training/course_detail.html", {"course": course})
