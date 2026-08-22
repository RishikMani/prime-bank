from django.db import models

from branch.models import Branch
from customer.models import Customer


class Account(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_column="account_id")
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="accounts"
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.PROTECT, related_name="accounts"
    )
    type = models.CharField(max_length=20, db_column="account_type")
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date = models.DateField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = "account"
