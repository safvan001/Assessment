from django.shortcuts import render
# scraping_app/views.py
from django.http import HttpResponse
from .scraping_module import scrape_properties

def scrape_data(request):
    # Call the scraping function
    scrape_properties()
    return HttpResponse("Scraping completed.")
# views.py
from django.shortcuts import render, redirect
from .models import ScrapingTask

def admin_dashboard(request):
    # Retrieve a list of all scraping tasks
    tasks = ScrapingTask.objects.all()
    return render(request, 'base.html', {'tasks': tasks})

def enable_disable_task(request, task_id):
    # Enable or disable a specific scraping task
    task = ScrapingTask.objects.get(pk=task_id)
    task.is_enabled = not task.is_enabled
    task.save()
    return redirect('admin_dashboard')

def change_schedule(request, task_id):
    # Allow changing the schedule for a specific scraping task
    if request.method == 'POST':
        new_schedule = request.POST['new_schedule']
        task = ScrapingTask.objects.get(pk=task_id)
        task.trigger_timing = new_schedule
        task.save()
    return redirect('admin_dashboard')

def trigger_task(request, task_id):
    # Manually trigger a specific scraping task
    # Implement the logic to start the scraping job here
    return redirect('admin_dashboard')


# Create your views here.
