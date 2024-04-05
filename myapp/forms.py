# forms.py

from django import forms
from .models import BookingReal

class BookingRealForm(forms.ModelForm):
    class Meta:
        model = BookingReal
        fields = ['name', 'email', 'description', 'address', 'eircode', 'guard']
