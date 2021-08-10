from django.contrib import admin
from . import models

@admin.register(models.Listing)
class ListingAdmin(admin.ModelAdmin):
     list_display = (
        'chores', 
        'title',
        'start_date', 
        'end_date' 
    )

    