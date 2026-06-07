from django.db import models

class Continent(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255, blank=True, default="")
    area = models.IntegerField(default=0)
    population = models.BigIntegerField(default=0)
    countries_number = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = "continent"

    def __str__(self):
        return self.name
