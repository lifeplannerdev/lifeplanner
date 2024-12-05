from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm  

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  
        else:
            
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    else:
        form = AppointmentForm()
        

    return render(request, 'home.html', {'form': form})


def service(request):
    return render(request,"services.html")
