import uuid


from django.core.exceptions import ValidationError
from django.db.models import Count, Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, date

from django.http import Http404
from rest_framework import request


# блокування введення меншої дати за поточну, it's working
def validate_past_time(value):
    today = now()
    if value < today:
        raise ValidationError(_(f'{value} вибраний час бронювання менший поточного {today} . Виберіть пізніший час'))


def validate_wish(value):
    prohibited_words = ['Путін', 'Шойгу']
    if value in prohibited_words:
        raise ValidationError(_(f'{value} is a prohibited word.'))


# validate pier 111, have priority 'def clean' (this validator don't working)
def validate_pier_check(value):
    pier_111 = BookingPier.objects.filter(pier_id=111).count()
    if pier_111 > 1:
        raise ValidationError(_(f'{value} test pier_id'))


class BookingPier(models.Model):
    # objects = None
    pier = models.ForeignKey('Pier', on_delete=models.PROTECT, null=True, verbose_name='Пірс')
    PIER_STATUS_CHOICES = [
        ("<span class='bk'>бронь</span>", "бронь"),
        ("<span class='fr'>вільний</span>", "вільний"),
    ]
    pier_status = models.CharField(max_length=40, choices=PIER_STATUS_CHOICES, default="бронь",
                                   verbose_name='Стан пірсу')
    time_booking_start = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                              verbose_name='Прибуття',
                                              validators=[validate_past_time]
                                              )  # , unique=True,
    time_booking_finish = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                               verbose_name='Відбуття',
                                               validators=[validate_past_time]
                                               )
    wish = models.CharField(max_length=255, verbose_name='Побажання', validators=[validate_wish])
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час публікації')
    is_published = models.BooleanField(default=True,
                                       # editable=False,  # the field is not displayed
                                       verbose_name='Підтверджую бронювання')
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)

    # block ChatGPT
    def clean(self):
        # check for overlapping bookings for the selected pier
        overlapping_bookings = BookingPier.objects.filter(
            pier=self.pier,
            time_booking_start__lte=self.time_booking_finish,
            time_booking_finish__gte=self.time_booking_start
        ).exclude(pk=self.pk)
        if overlapping_bookings.exists():
            raise ValidationError(_("На вибраний Вами час пірс вже заброньований. Оберіть інший час або пірс"))
    # endblock

    class Meta:
        verbose_name = 'Бронювання пірсу'
        verbose_name_plural = 'Бронювання пірсів'
        ordering = ['id']


class Pier(models.Model):
    name = models.CharField(max_length=100, db_index=True, validators=[validate_pier_check], verbose_name='Місце')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пірс'
        verbose_name_plural = 'Пірси'
        ordering = ['id']
