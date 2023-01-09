from django.db import models

# Create your models here.
class CommonModel(models.Model):

    """Common Model Definitinon"""

    create_at = models.DateTimeField(
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
