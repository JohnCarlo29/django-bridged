from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(blank=True, max_length=100, verbose_name='first name')
    middle_name = models.CharField(blank=True, max_length=100, verbose_name='middle name')
    last_name = models.CharField(blank=True, max_length=100, verbose_name='last name')
    contact_no = models.CharField(blank=True, max_length=12, verbose_name='contact number')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
