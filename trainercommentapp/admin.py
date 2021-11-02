from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from trainercommentapp.models import TrainerComment


class TrainerCommentAdmin(admin.ModelAdmin):
    list_display = ('trainer',
                    'member',
                    'content')


admin.site.register(TrainerComment, TrainerCommentAdmin)