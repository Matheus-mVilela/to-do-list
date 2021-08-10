from django.contrib import admin
from . import models

@admin.register(models.Chore)
class ChoresAdmin(admin.ModelAdmin):
     list_display = (
        'title',
        'description',
    )

    


