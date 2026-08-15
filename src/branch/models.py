from django.db import models


class Branch(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    opened_date = models.DateField()
    ifsc = models.CharField(max_length=12)

    class Meta:
        db_table = "branch"
