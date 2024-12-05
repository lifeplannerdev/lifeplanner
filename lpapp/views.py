from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm  
from .forms import WebinarForm  

from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm, WebinarForm

def home(request):
    if request.method == 'POST':
        if 'appointment' in request.POST:  
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': form.errors.as_json()})
        elif 'webinar' in request.POST:  
            form = WebinarForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': form.errors.as_json()})
    else:
        appointment_form = AppointmentForm()
        webinar_form = WebinarForm()

    return render(request, 'home.html', {'appointment_form': appointment_form, 'webinar_form': webinar_form})



def service(request):
    return render(request,"services.html")
