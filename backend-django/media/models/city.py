from django.db import models

from .country import Country

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country,
        db_column="country_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="cities",
    )
    capital = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "city"

    def __str__(self):
        return self.name
