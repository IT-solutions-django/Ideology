from django.db import models


class SpecialOffer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    date = models.CharField(max_length=150, verbose_name='Дата в виде текста')
    main_desc = models.CharField(max_length=150, verbose_name='Главное описание')
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    date = models.CharField(max_length=150, verbose_name='Дата в виде текста')
    main_desc = models.CharField(max_length=150, verbose_name='Главное описание')
    desc = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='certificate', verbose_name='Фото')

    def __str__(self):
        return self.name


class About(models.Model):
    numb_1 = models.CharField(max_length=50, verbose_name='В сфере медицины')
    numb_2 = models.CharField(max_length=50, verbose_name='Специалистов в штабе')
    numb_3 = models.CharField(max_length=50, verbose_name='Довольных пациентов')
    numb_4 = models.CharField(max_length=50, verbose_name='Лицензированных аппаратов')

    def __str__(self):
        return 'Информация о компании в блоке о нас'


class DescSubscription(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    main_desc = models.CharField(max_length=150, verbose_name='Главное описание')
    photo = models.ImageField(upload_to='subscription', verbose_name='Фото')
    old_price = models.DecimalField(max_digits=12, decimal_places=1, verbose_name='Старая цена')
    new_price = models.DecimalField(max_digits=12, decimal_places=1, verbose_name='Новая цена')
    desc = models.ManyToManyField(DescSubscription, verbose_name='Список содержимого абонемента')

    def __str__(self):
        return self.name


class Scope(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name


class Specialist(models.Model):
    experience = models.PositiveIntegerField(verbose_name='Стаж')
    name = models.CharField(max_length=150, verbose_name='ФИ специалиста')
    photo = models.ImageField(upload_to='specialist', verbose_name='Фото')
    desc = models.TextField(verbose_name='Описание')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Сфера деятельности')

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    time = models.PositiveSmallIntegerField(verbose_name='Время прочтения')
    photo = models.ImageField(upload_to='news', verbose_name='Фото')
    main_desc = models.TextField(verbose_name='Вступительная часть новости')
    desc = models.TextField(verbose_name='Текст новости')

    def __str__(self):
        return self.name


class Contact(models.Model):
    main_phone = models.CharField(max_length=50, verbose_name='Главный телефон')
    phone = models.CharField(max_length=50, verbose_name='Второй телефон')
    email = models.CharField(max_length=50, verbose_name='Почта')
    schedule = models.CharField(max_length=150, verbose_name='График работы')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return self.address


class Vacancies(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    requirement = models.CharField(max_length=150, verbose_name='Требование')

    def __str__(self):
        return self.name


class Licenses(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    photo = models.ImageField(upload_to='licenses', verbose_name='Фото')

    def __str__(self):
        return self.name


class ListProcedures(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=12, decimal_places=1, verbose_name='Цена')

    def __str__(self):
        return self.name


class Procedures(models.Model):
    procedure = models.ManyToManyField(ListProcedures, verbose_name='Процедуры')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Сфера деятельности')

    def __str__(self):
        return self.scope.name





