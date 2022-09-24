from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    def get_full_name(self) -> str:
        return f"{self.last_name}{self.first_name}"
