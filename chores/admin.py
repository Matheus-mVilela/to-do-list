from django.contrib import admin
from . import models

@admin.register(models.Chore)
class ChoresAdmin(admin.ModelAdmin):
     list_display = (
        'id_chore',
        'title',
        'description',
    )

    


