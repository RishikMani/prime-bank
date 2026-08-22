from django.db import models


class Branch(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column="branch_id")
    branch_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    opening_date = models.DateField()
    ifsc = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "branch"
