from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import AutoField

# Create your models here.

class TotalVote(models.Model):
    total_vote = models.BigIntegerField()

class Leader(models.Model):
    image = models.ImageField(upload_to = 'pics', blank=True, null=True)
    name = models.CharField(max_length=100)
    nishan = models.ImageField(upload_to='pics', blank=True, null=True)
    vote = models.BigIntegerField()
    order = models.SmallIntegerField(default=0, editable=True)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name
