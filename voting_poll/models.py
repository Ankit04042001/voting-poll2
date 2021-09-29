from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import AutoField

# Create your models here.

class TotalVote(models.Model):
    total_vote = models.BigIntegerField()

class Leader(models.Model):
    image = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    nishan = models.CharField(max_length=100)
    vote = models.BigIntegerField()
    order = models.SmallIntegerField(default=0, editable=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name
