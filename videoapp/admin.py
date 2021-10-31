from django.contrib import admin

# Register your models here.
from videoapp.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'url',
                    'tags',
                    'hits',
                    )


admin.site.register(Video, VideoAdmin)