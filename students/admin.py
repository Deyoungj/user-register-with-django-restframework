from importlib.resources import Package
from django.contrib import admin
from .models import Student, Package, PackageEnroled, Tutor

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Package)
admin.site.register(PackageEnroled)
