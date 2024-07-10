from django.urls import path
from .views import login_view, student_dashboard, staff_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('staff_dashboard/', staff_dashboard, name='staff_dashboard'),
]
