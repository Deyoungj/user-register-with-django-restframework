
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


from .custom_manager import CustomUserManager

Role = (('admin','admin'), ('staff','staff'))


class CustomUser(AbstractBaseUser,PermissionsMixin):
    fullname = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=Role)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)


    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['fullname']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at',)

    
    

