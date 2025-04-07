from django.shortcuts import render
from .models import HomePageContent, AboutPage, ContactPage, TermsOfService, PrivacyPolicy
from .forms import ApplicationForm
from django.http import JsonResponse


def home(request):
    """Главная страница."""
    homepage_content = HomePageContent.objects.first()
    context = {
        'homepage_content': homepage_content,
        'instructor': homepage_content.instructor if homepage_content else None,
        'discount_title': homepage_content.discount_title if homepage_content else None,
        'discount_description': homepage_content.discount_description if homepage_content else None,
        'discount_percentage': homepage_content.discount_percentage if homepage_content else None,
        'original_price': homepage_content.original_price if homepage_content else None,
        'discounted_price': homepage_content.discounted_price if homepage_content else None,
        'instructor_room_photo': (
            homepage_content.instructor.room_photo.url
            if homepage_content and homepage_content.instructor and
            homepage_content.instructor.room_photo else None
        ),
        'events': homepage_content.events.all() if homepage_content else [],
    }
    return render(request, 'home/home.html', context)


def about(request):
    """Страница 'О нас'."""
    about_page = AboutPage.objects.first()
    instructors = about_page.instructors.all() if about_page else []
    context = {
        'about_page': about_page,
        'instructors': instructors,
    }
    return render(request, 'about/about.html', context)

def contacts(request):
    """Страница контактов."""
    contact_info = ContactPage.objects.first()
    return render(request, 'contacts/contacts.html', {'contact_info': contact_info})


def terms_of_service(request):
    """Условия использования."""
    terms = TermsOfService.objects.first()
    return render(request, 'main/terms_of_policy.html', {'terms': terms})


def privacy_policy(request):
    """Политика конфиденциальности."""
    policy = PrivacyPolicy.objects.first()
    return render(request, 'main/policy.html', {'policy': policy})


def application_view(request):
    """Форма заявки."""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Ваша заявка успешно отправлена!'
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ApplicationForm()
    return render(request, 'application/application.html', {'form': form})


def application_success(request):
    """Успешная заявка."""
    return render(request, 'application/application_success.html')
