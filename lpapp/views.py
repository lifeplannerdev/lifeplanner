from django.http import JsonResponse
from django.shortcuts import render
from .forms import AppointmentForm  # Ensure the form is imported

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Return a JSON response on success
        else:
            # Return specific error messages if the form isn't valid
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    else:
        form = AppointmentForm()

    return render(request, 'home.html', {'form': form})