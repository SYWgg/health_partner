from django.contrib import admin

# Register your models here.
from commentapp.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('board',
                    'writer',
                    'content')


admin.site.register(Comment, CommentAdmin)