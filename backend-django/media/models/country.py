from django.db import models

from .continent import Continent

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255, blank=True, default="")
    continent = models.ForeignKey(
        Continent,
        db_column="continent_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="countries",
    )
    iso_numeric = models.CharField(max_length=50)
    iso_alpha2 = models.CharField(max_length=50)
    iso_alpha3 = models.CharField(max_length=50)
    flag = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "country"

    def __str__(self):
        return self.name
