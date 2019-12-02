from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Sick(models.Model):
    name = models.CharField(verbose_name='Назва', db_index=True, unique=True, max_length=64)
    description = models.CharField(verbose_name='Опис', max_length=250)
    symptoms = models.CharField(verbose_name='Симптоми', max_length=250)
    cure = models.CharField(verbose_name='Лікування', max_length=250)

    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
