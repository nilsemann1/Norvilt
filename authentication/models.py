from os import O_WRONLY
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser, 
    PermissionsMixin
)

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password, **extra_fields): 
        email = self.normalize_email(email)

        user = User.objects.create(email=email, **extra_fields)
        # Krypter passordet før man lagrer det i databasen
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'date_of_birth', 'address', 'password']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.email) 
