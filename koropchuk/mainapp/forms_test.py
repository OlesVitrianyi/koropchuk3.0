from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


# class BookingAPierForm(forms.ModelForm):
#     def __init__(self, *arg, **kwargs):
#         super().__init__(*arg, **kwargs)
#         self.fields['pier'].empty_label = 'Оберіть пірс'
#
#     class Meta:
#         model = Guest
#         fields = ['guest_name', 'phone_number', 'comment', 'pier', 'pier_status', 'is_published']
#         widgets = {
#             'guest_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
#         }
#
#     def clean_guest_name(self):
#         guest_name = self.cleaned_data['guest_name']
#         if len(guest_name) > 40:
#             raise ValidationError('Довжина перевищує 200 символів')
#
#         return guest_name


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#    PIER_STATUS_CHOICES = [
        #        ('bk', 'booking'),
        #        ('bk', 'замовлено'),
#        ('<span class="bk">бронь</span>', 'бронь'),
        #        ('fr', 'free'),
        #        ('fr', 'вільно'),
#        ('<span class="fr">вільно</span>', 'вільно'),
#    ]
#    guest_name = forms.CharField(max_length=40)
    #    phone_number = forms.PhoneNumberField()
#    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#    pier_status = forms.ModelChoiceField(queryset=Guest.objects.pier_status.all()
#    is_published = forms.BooleanField()
#    pier = forms.ModelChoiceField(queryset=Pier.objects.all())
