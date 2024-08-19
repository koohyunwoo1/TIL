from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=128, blank=True)
    good_seller = models.ManyToManyField('self', symmetrical=False, related_name='my_customers')
    image = models.ImageField(blank=True, upload_to='user_profile/')