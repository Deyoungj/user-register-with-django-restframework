from datetime import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.db import models
from random import choice
import string

def generate_student_id():
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(15))

GENDER_CHOICES = [('male', 'male'), ('female', 'female'),]

class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    months = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255,null=True)
    student_id = models.CharField(editable=False, unique=True, max_length=20,default=generate_student_id)
    image = models.ImageField(upload_to='images', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email


class PackageEnroled(models.Model):
    package = models.ForeignKey(Package, related_name='package', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student', on_delete=models.SET_NULL, null=True)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)


    def save(self,*args, **kwargs):
        months= self.package.months
        self.due_date = timezone.now() + relativedelta(months=int(months))
        
        return super(PackageEnroled, self).save(*args, **kwargs)


    def __str__(self):
        return f'name: {self.student.fullname} package: {self.package.name} on: {self.date_enrolled}'


