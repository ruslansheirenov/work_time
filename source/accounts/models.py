from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    organization = models.ManyToManyField('webapp.Organization', related_name='user_organization')
    email = models.EmailField(verbose_name='Email', unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + "'s Profile"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'