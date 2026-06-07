from django.db import models

from .person import Person
from .profession import Profession

class PersonProfession(models.Model):
    person = models.ForeignKey(
        Person,
        db_column="person_id",
        on_delete=models.DO_NOTHING,
    )
    profession = models.ForeignKey(
        Profession,
        db_column="profession_id",
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False
        db_table = "person_profession"
        unique_together = (("person", "profession"),)

    def __str__(self):
        return f"{self.person} - {self.profession}"
