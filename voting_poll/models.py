from django.contrib.admin import options
from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import AutoField
import cloudinary 
from cloudinary.models import CloudinaryField

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

class Audio(models.Model):
    click_sound = CloudinaryField(resource_type="raw")

    def __str__(self):
        return f"Click Sound : {self.click_sound}"
