from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MerlinUser

admin.site.register(MerlinUser, UserAdmin)