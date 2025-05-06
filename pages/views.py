from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def stock(request):
    return render(request, 'stock.html')


def licenses(request):
    return render(request, 'licenses.html')


def contacts(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def vacancies(request):
    return render(request, 'vacancies.html')


def news(request):
    return render(request, 'news.html')


def card_news(request):
    return render(request, 'card-news.html')


def services(request):
    return render(request, 'services.html')


def hardware_cosmetology(request):
    return render(request, 'hardware_cosmetology.html')


def care_procedures(request):
    return render(request, 'care_procedures.html')

