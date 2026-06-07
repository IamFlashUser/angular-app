from django.db import models

from .city import City
from .country import Country
from .profession import Profession

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    birth_city = models.ForeignKey(
        City,
        db_column="birth_city_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="born_persons",
    )
    death_date = models.DateField(null=True, blank=True)
    death_city = models.ForeignKey(
        City,
        db_column="death_city_id",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="dead_persons",
    )
    gender_id = models.BigIntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    nationalities = models.ManyToManyField(
        Country,
        through="PersonNationality",
        related_name="persons",
    )
    professions = models.ManyToManyField(
        Profession,
        through="PersonProfession",
        related_name="persons",
    )

    class Meta:
        managed = False
        db_table = "person"

    def __str__(self):
        return self.name
