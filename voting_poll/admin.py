from django.contrib import admin

# Register your models here.

from .models import TotalVote, Leader, Audio, UserIp

admin.site.register(TotalVote)
admin.site.register(Leader)
admin.site.register(Audio)
admin.site.register(UserIp)