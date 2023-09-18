"""
URL configuration for assessment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Scraper import views
app_name="Scraper"

urlpatterns = [
    # ... other URL patterns ...

    # URL for scraping data
    path('scrape/', views.scrape_data, name='scrape_data'),

    # URL for the admin dashboard
    path('', views.admin_dashboard, name='admin_dashboard'),

    # URL for enabling/disabling a task
    path('admin/enable_disable/<int:task_id>/', views.enable_disable_task, name='enable_disable_task'),

    # URL for changing the schedule of a task
    path('admin/change_schedule/<int:task_id>/', views.change_schedule, name='change_schedule'),

    # URL for triggering a task
    path('admin/trigger_task/<int:task_id>/', views.trigger_task, name='trigger_task'),
]


