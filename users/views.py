from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from .models import User

def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == User.SERVICE_NUMBER:
                return redirect('student_dashboard')
            elif user.user_type == User.PAYROLL_NUMBER:
                return redirect('staff_dashboard')
    return render(request, 'users/login.html', {'form': form})

def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')

def staff_dashboard(request):
    return render(request, 'users/staff_dashboard.html')
