from django.contrib.auth.models import (BaseUserManager,PermissionsMixin, AbstractBaseUser)


class CustomUserManager(BaseUserManager):


    def create_superuser(self, email,password,**extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must  have is_superuser")

        if not email:
            raise ValueError("email must be provided")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

