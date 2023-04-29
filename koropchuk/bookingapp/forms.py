from django import forms
from .models import *

# from django.contrib.auth.forms import AuthenticationForm
# from django.core.exceptions import ValidationError
#
# from .models import *


class BookingAPierForm(forms.Form):
    # pier = forms.ForeignKey()
    pier = forms.ModelChoiceField(queryset=Pier.objects.all())
    pier_status = forms.CharField(max_length=40)
    time_booking_start = forms.DateTimeField()
    time_booking_finish = forms.DateTimeField()
    wish = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
