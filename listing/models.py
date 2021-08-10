from django.db import models



from django.db.models.fields import DateField, DateTimeField
from chores.models import Chore

class Listing(models.Model):
    id_listing = models.AutoField(primary_key=True)
    chores = models.ForeignKey(Chore, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title