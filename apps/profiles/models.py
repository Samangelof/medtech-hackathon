from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNet(AbstractUser):

    first_login = models.DateTimeField(verbose_name='Первый вход', auto_now=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20)
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class Maternity(models.Model):

    name = models.CharField(verbose_name='Имя роддома', max_length=200)
    type = models.CharField(verbose_name='Тип', max_length=400)
    phone = models.CharField(verbose_name='Контакты', max_length=200)
    address = models.CharField(verbose_name='Адрес', max_length=200)
    image = models.ImageField(verbose_name='Картинка',  null=True, upload_to='resource')

    class Meta:
        verbose_name = "Роддом"
        verbose_name_plural = "Роддомы"


class Doctors(models.Model):

    name = models.CharField(verbose_name='Имя Врача', max_length=40)
    area_of_specialization = models.CharField(verbose_name='Область специализации', max_length=300)
    work_experience = models.CharField(verbose_name='Стаж работы', max_length=50)
    place_of_work = models.CharField(verbose_name='Место работы', max_length=100)
    address_of_work = models.CharField(verbose_name='Адресс работы', max_length=100)
    image = models.ImageField(verbose_name='Автатар врача',  null=True, upload_to='resource')

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

