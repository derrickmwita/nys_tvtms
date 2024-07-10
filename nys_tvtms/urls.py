"""
URL configuration for nys_tvtms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from users.views import login_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL (home page)
    path('login/', views.login_view, name='login'),  # Login page
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),  # Student dashboard
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),  # Staff dashboard
]