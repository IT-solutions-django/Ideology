from django.shortcuts import render
from .models import Contact, SpecialOffer, Certificate, About, Subscription, Specialist, News, Licenses, Vacancies


def home(request):
    contact = Contact.objects.first()
    special_offer = SpecialOffer.objects.all()[:2]
    certificate = Certificate.objects.all()[:6]
    about_info = About.objects.first()
    subscription = Subscription.objects.all()[:4]
    specialist = Specialist.objects.all()
    news_info = News.objects.all()[:2]

    return render(
        request,
        'home.html',
        {
            'contact': contact,
            'special_offer': special_offer,
            'certificate': certificate,
            'about_info': about_info,
            'subscription': subscription,
            'specialist': specialist,
            'news_info': news_info
        }
    )


def stock(request):
    contact = Contact.objects.first()
    special_offer = SpecialOffer.objects.all()
    certificate = Certificate.objects.all()
    subscription = Subscription.objects.all()

    return render(
        request,
        'stock.html',
        {
            'contact': contact,
            'special_offer': special_offer,
            'certificate': certificate,
            'subscription': subscription,
        }
    )


def licenses(request):
    licenses_info = Licenses.objects.all()

    return render(request, 'licenses.html', {
        'licenses_info': licenses_info
    })


def contacts(request):
    contact = Contact.objects.first()
    licenses_info = Licenses.objects.all()

    return render(request, 'contact.html', {
        'licenses_info': licenses_info,
        'contact': contact
    })


def about(request):
    about_info = About.objects.first()
    specialist = Specialist.objects.all()

    return render(request, 'about.html',
        {
            'about_info': about_info,
            'specialist': specialist,
        }
    )


def vacancies(request):
    vacancies_info = Vacancies.objects.all()

    return render(request, 'vacancies.html', {
        'vacancies_info': vacancies_info
    })


def news(request):
    news_info = News.objects.all()

    return render(request, 'news.html', {
        'news_info': news_info
    })


def card_news(request, news_id):
    news_info = News.objects.get(id=news_id)

    next_news = News.objects.filter(id__gt=news_id).order_by('id').first() or news_info

    prev_news = News.objects.filter(id__lt=news_id).order_by('-id').first() or news_info

    return render(request, 'card-news.html', {
        'news_info': news_info,
        'next_news': next_news,
        'prev_news': prev_news
    })


def services(request):
    return render(request, 'services.html')


def hardware_cosmetology(request):
    specialist = Specialist.objects.all()

    return render(request, 'hardware_cosmetology.html', {
        'specialist': specialist
    })


def care_procedures(request):
    specialist = Specialist.objects.all()

    return render(request, 'care_procedures.html', {
        'specialist': specialist
    })


def massage(request):
    specialist = Specialist.objects.all()

    return render(request, 'massage.html', {
        'specialist': specialist
    })


def peeling(request):
    specialist = Specialist.objects.all()

    return render(request, 'peeling.html', {
        'specialist': specialist
    })


def procedures_for_men(request):
    specialist = Specialist.objects.all()

    return render(request, 'procedures_for_men.html', {
        'specialist': specialist
    })


def spa(request):
    specialist = Specialist.objects.all()

    return render(request, 'spa.html', {
        'specialist': specialist
    })
