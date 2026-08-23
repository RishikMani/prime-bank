import pytest

from django.db.utils import DataError, IntegrityError

from account.models import Account
from base import settings
from branch.models import Branch
from customer.models import Customer


# update the HOST in Django settingsto point to localhost
settings.DATABASES["default"]["HOST"] = "localhost"


@pytest.fixture
def branch():
    return Branch.objects.create(
        id=1,
        branch_name="Main Branch",
        city="Mumbai",
        state="Maharashtra",
        opening_date="2020-01-01",
        ifsc="ABCD0123456",
    )


@pytest.fixture
def customer():
    return Customer.objects.create(
        id=1,
        name="Andre Gomez",
        gender="male",
        dob="1988-04-26",
        city="Gonda",
        state="Uttar Pradesh",
        phone="9999999999",
        email="andre.gomez@example.com",
        occupation="freelancer",
        income=456725.98,
        joining_date="2012-03-12",
        credit_score=800,
    )


@pytest.mark.django_db(transaction=True)
class TestModel:
    def test_create_account_without_existing_customer(self, branch):
        """Create an account when the customer does not exist yet.

        It should raise an IntegrityError.
        """
        assert not Customer.objects.filter(pk=1).exists()

        with pytest.raises(IntegrityError):
            Account.objects.create(
                id=1,
                customer_id=1,
                branch=branch,
                type="savings",
                balance=13456,
                opening_date="2013-06-27",
                status="active",
            )

    def test_create_account_without_existing_branch(self, customer):
        """Create an account when the branch does not exist yet.

        It should raise an IntegrityError.
        """
        assert not Branch.objects.filter(pk=1).exists()

        with pytest.raises(IntegrityError):
            Account.objects.create(
                id=1,
                customer=customer,
                branch_id=1,
                type="savings",
                balance=13456,
                opening_date="2013-06-27",
                status="active",
            )

    def test_create_an_account_with_type_more_than_20_characters(
        self, branch, customer
    ):
        with pytest.raises(DataError):
            Account.objects.create(
                id=1,
                customer=customer,
                branch=branch,
                type="more than 20 characters long",
                balance=13456,
                opening_date="2013-06-27",
                status="active",
            )

    def test_create_an_account_with_balance_more_than_10_digits(
        self, branch, customer
    ):
        with pytest.raises(DataError):
            Account.objects.create(
                id=1,
                customer=customer,
                branch=branch,
                type="savings",
                balance=12345678901,
                opening_date="2013-06-27",
                status="active",
            )

    def test_create_an_account_with_status_more_than_10_characters(
        self, branch, customer
    ):
        with pytest.raises(DataError):
            Account.objects.create(
                id=1,
                customer=customer,
                branch=branch,
                type="savings",
                balance=12345678901,
                opening_date="2013-06-27",
                status="more than 10 characters",
            )
