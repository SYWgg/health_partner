from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from accountapp.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'name',
        'is_trainer',
        'trainer_num',
        'level',
        'date_joined'
        )
    search_fields = ('user_id', 'name', 'is_trainer')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)    # Admin페이지의 GROUP삭제