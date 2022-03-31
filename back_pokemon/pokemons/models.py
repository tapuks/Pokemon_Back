from django.db import models


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField(blank=True, null=True)
    exp = models.IntegerField()
    libre = models.BooleanField(default=True)

    # exp_next_level = models.IntegerField()
    # exp_derrota = models.IntegerField( blank=True, null=True)


    def __str__(self):
        return self.name


