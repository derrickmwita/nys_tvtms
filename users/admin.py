from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Staff

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Staff)
