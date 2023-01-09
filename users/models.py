from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        Male = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoice(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoice(models.TextChoices):
        WON = ("won", "Korean WON")
        USD = ("usd", "Dollar")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    # is_host = models.BooleanField(null=True)
    avata = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=20,
        choices=GenderChoice.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoice.choices,
    )
    currency = models.CharField(
        max_length=10,
        choices=CurrencyChoice.choices,
    )
