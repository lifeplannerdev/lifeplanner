from django import forms
from .models import Appointment
from .models import Webinar

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['name','mail']        