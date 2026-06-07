from django.db import models

class Profession(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = "profession"

    def __str__(self):
        return self.name
