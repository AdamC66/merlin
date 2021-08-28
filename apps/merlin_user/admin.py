from django.contrib import admin
from .models import MerlinUser

admin.site.register(MerlinUser, admin.ModelAdmin)