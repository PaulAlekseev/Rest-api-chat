import datetime

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.validators import MaxValueValidator


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a User instance with the given username, email,
        date of birth and password.
        """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a superuser instance with the given username, email,
        date of birth and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    username = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField(
        validators=[MaxValueValidator(limit_value=datetime.date.today())],
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']