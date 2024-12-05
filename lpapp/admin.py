from django.contrib import admin
from . models import Appointment
from . models import Webinar
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Webinar)
