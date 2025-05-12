"""
URL configuration for ideology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home, stock, licenses, contacts, about, vacancies, news, card_news, services, hardware_cosmetology, care_procedures, massage, peeling, procedures_for_men, spa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stock/', stock, name='stock'),
    path('licenses/', licenses, name='licenses'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('vacancies/', vacancies, name='vacancies'),
    path('news/', news, name='news'),
    path('card-news/', card_news, name='card-news'),
    path('services/', services, name='services'),
    path('hardware_cosmetology/', hardware_cosmetology, name='hardware_cosmetology'),
    path('care_procedures/', care_procedures, name='care_procedures'),
    path('massage/', massage, name='massage'),
    path('peeling/', peeling, name='peeling'),
    path('procedures_for_men/', procedures_for_men, name='procedures_for_men'),
    path('spa/', spa, name='spa'),
]
