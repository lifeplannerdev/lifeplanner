from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm,WebinarForm  

def home(request):
    if request.method == 'POST':
        # Check if the form submission is for the AppointmentForm
        if 'firstname' in request.POST:
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': appointment_form.errors.as_json()})
        
        # Check if the form submission is for the EnrollmentForm
        elif 'name' in request.POST:
            enrollment_form = WebinarForm(request.POST)
            if enrollment_form.is_valid():
                enrollment_form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': enrollment_form.errors.as_json()})
    
    # Handle GET requests
    else:
        appointment_form = AppointmentForm()
        enrollment_form = WebinarForm()
    
    return render(request, 'home.html', {
        'form': appointment_form,
        'enrollment_form': enrollment_form,
    })



def service(request):
    return render(request,"services.html")
