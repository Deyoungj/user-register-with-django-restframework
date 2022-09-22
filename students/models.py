from datetime import datetime
from enum import unique
from dateutil.relativedelta import relativedelta
from django.db import models
from random import choice
import string

def generate_student_id():
    id_code = ''.join(choice(string.ascii_letters + string.digits) for _ in range(15))
    return id_code

GENDER_CHOICES = [('male', 'male'), ('female', 'female'),]

class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    months = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} {self.price}'

class Student(models.Model):
    fullname = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255,null=True)
    student_id = models.CharField(default=generate_student_id())
    image = models.FileField(upload_to='images')


    def __str__(self):
        return f'{self.fullname} {self.email}'


class PackageEnroled(models.Model):
    package = models.ForeignKey(Package, related_name='packages', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)


    def save(self,*args, **kwargs):
        months= self.package.months
        due_date = datetime.now() + relativedelta(months=months)
        return super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.student.fullname} {self.packages.name} on {self.date_enrolled}'


