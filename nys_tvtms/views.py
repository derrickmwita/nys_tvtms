from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')