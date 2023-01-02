from django.db import models

# Create your models here.


class House(models.Model):

    """Model difinition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="price", help_text="정수만 입력가능")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allow = models.BooleanField(default=True, verbose_name="Pet_Allowed")

    def __str__(self):
        return self.name