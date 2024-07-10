from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    SERVICE_NUMBER = 'SN'
    PAYROLL_NUMBER = 'PN'
    USER_TYPE_CHOICES = [
        (SERVICE_NUMBER, 'Service Number'),
        (PAYROLL_NUMBER, 'Payroll Number'),
    ]
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=SERVICE_NUMBER)
    service_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    payroll_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change this related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Change this related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_no = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    id_no = models.CharField(max_length=50)
    guardian = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('courses.Subject')
    progress = models.JSONField()

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payroll_no = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=50)
    subjects = models.ManyToManyField('courses.Subject')
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)


