from django.contrib import admin

# Register your models here.
from profileapp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')