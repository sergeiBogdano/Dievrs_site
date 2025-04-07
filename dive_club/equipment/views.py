from django.shortcuts import render, get_object_or_404
from .models import Equipment, EquipmentCategory, EquipmentPageContent


def equipment_list(request):
    """Страница ремонта оборудования."""
    equipment_page_content = EquipmentPageContent.objects.first()
    equipment_categories = EquipmentCategory.objects.all()

    category_name = request.GET.get('category')
    if category_name:
        equipment_list = Equipment.objects.filter(category__name=category_name)
    else:
        equipment_list = Equipment.objects.all()

    context = {
        'equipment_list': equipment_list,
        'equipment_page_content': equipment_page_content,
        'equipment_categories': equipment_categories,
        'selected_category': category_name,
    }
    return render(request, 'equipment/equipment_list.html', context)


def equipment_detail(request, pk):
    """Детальная страница ремонта оборудования."""
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment})
