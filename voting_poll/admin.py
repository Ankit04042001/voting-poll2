from django.contrib import admin

# Register your models here.

from .models import TotalVote, Leader

admin.site.register(TotalVote)
admin.site.register(Leader)