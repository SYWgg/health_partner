from django.contrib import admin

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'writer',
                    'image',
                    'hits',
                    'created_at')


admin.site.register(Board, BoardAdmin)