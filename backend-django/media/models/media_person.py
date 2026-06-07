from django.db import models

from .media import Media
from .person import Person
from .profession import Profession

class MediaPerson(models.Model):
    media = models.ForeignKey(
        Media,
        db_column="media_id",
        on_delete=models.DO_NOTHING,
    )
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
        db_table = "media_person"
        unique_together = (("media", "person", "profession"),)

    def __str__(self):
        return f"{self.media} - {self.person} - {self.profession}"
