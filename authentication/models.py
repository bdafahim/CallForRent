from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)



_GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
    ('*', 'Not to say'),
)


class Account(AbstractBaseUser):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=1, choices=_GENDER)
    active = models.BooleanField(default=True) #can log in
    staff = models.BooleanField(default=False) #staff user not super user
    admin = models.BooleanField(default=False) #superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

