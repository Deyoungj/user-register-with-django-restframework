from email.policy import default
from django.db import models
from random import choice, choices
import string

def generate_student_id():
    id_code = ''.join(choice(string.ascii_letters + string.digits) for _ in range(15))
    return id_code

GENDER_CHOICES = [('male', 'male'), ('female', 'female'),]

class Packages(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Students(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    student_id = models.CharField(default=generate_student_id())
    image = models.FileField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.email}'

class PackageInstance(models.Model):
    pass
