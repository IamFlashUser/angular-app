from django.db import models

from .country import Country
from .person import Person

class PersonNationality(models.Model):
    person = models.ForeignKey(
        Person,
        db_column="person_id",
        on_delete=models.DO_NOTHING,
    )
    country = models.ForeignKey(
        Country,
        db_column="country_id",
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False
        db_table = "person_nationality"
        unique_together = (("person", "country"),)

    def __str__(self):
        return f"{self.person} - {self.country}"
