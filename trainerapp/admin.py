from django.contrib import admin

# Register your models here.
from trainerapp.models import Trainer


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer',
                    'name',
                    'img',
                    'trainer_intro',
                    'program_intro',
                    'charge',
                    'training_time',
                    'career',
                    'created_at',
                    )


admin.site.register(Trainer, TrainerAdmin)