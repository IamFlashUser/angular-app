from django.db import models

from .media_type import MediaType
from .person import Person

class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(
        MediaType,
        db_column="type_id",
        on_delete=models.DO_NOTHING,
        related_name="medias",
    )
    release_year = models.SmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    persons = models.ManyToManyField(
        Person,
        through="MediaPerson",
        related_name="medias",
    )

    class Meta:
        managed = False
        db_table = "media"

    def __str__(self):
        return self.title
