from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class tb1_Authentication(AbstractBaseUser):
    Empcode = models.IntegerField()
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.username
    
# adminapp/models.py



    

