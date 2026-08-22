from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.PositiveIntegerField(primary_key=True, db_column="customer_id")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    dob = models.DateField(db_column="date_of_birth")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True, max_length=50)
    occupation = models.CharField(max_length=50)
    income = models.DecimalField(
        max_digits=12, decimal_places=2, db_column="annual_income"
    )
    joining_date = models.DateField()
    credit_score = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "customer"
