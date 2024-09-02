# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserRole(models.TextChoices):
    NON_MEMBER = 'NON_MEMBER', '동아리 소속 아님'
    MEMBER = 'MEMBER', '동아리 회원'
    EXECUTIVE = 'EXECUTIVE', '동아리 임원'

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.NON_MEMBER,
    )
