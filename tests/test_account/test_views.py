from decimal import Decimal

import pytest

from rest_framework.test import APIClient

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


@pytest.fixture
def accounts(branch, customer):
    return Account.objects.bulk_create(
        [
            Account(
                id=1,
                customer=customer,
                branch=branch,
                type="savings",
                balance=13456,
                opening_date="2013-06-27",
                status="active",
            ),
            Account(
                id=2,
                customer=customer,
                branch=branch,
                type="fixed",
                balance=13456,
                opening_date="2013-06-27",
                status="closed",
            ),
            Account(
                id=3,
                customer=customer,
                branch=branch,
                type="salary",
                balance=13456,
                opening_date="2013-06-27",
                status="dormant",
            ),
            Account(
                id=4,
                customer=customer,
                branch=branch,
                type="savings",
                balance=274568,
                opening_date="2013-06-27",
                status="active",
            ),
        ]
    )


@pytest.mark.django_db
class TestViews:
    client = APIClient()

    def test_account_count_by_status(self, accounts):
        response = self.client.get("/account/count-by-status/")
        assert response.status_code == 200
        assert "counts" in response.data.keys()
        assert len(response.data["counts"]) == 3
        assert response.data["counts"]["active"] == 2
        assert response.data["counts"]["closed"] == 1
        assert response.data["counts"]["dormant"] == 1

    def test_account_count_by_account_type(self, accounts):
        response = self.client.get("/account/count-by-account-type/")
        assert response.status_code == 200
        assert "counts" in response.data.keys()
        assert len(response.data["counts"]) == 3
        assert response.data["counts"]["savings"] == 2
        assert response.data["counts"]["salary"] == 1
        assert response.data["counts"]["fixed"] == 1

    def test_total_available_balance_per_account_type(self, accounts):
        response = self.client.get("/account/total-balance-per-account-type/")
        assert response.status_code == 200
        assert "balance" in response.data.keys()
        assert len(response.data["balance"]) == 3
        assert response.data["balance"]["savings"] == Decimal("288024.00")
        assert response.data["balance"]["salary"] == Decimal("13456.00")
        assert response.data["balance"]["fixed"] == Decimal("13456.00")

    def test_number_of_accounts_opened(self, accounts):
        response = self.client.get("/account/total-number-of-accounts/")
        assert response.status_code == 200
        assert "total_number_of_accounts" in response.data.keys()
        assert response.data["total_number_of_accounts"] == 4

    def test_average_balance_all_accounts(self, accounts):
        response = self.client.get("/account/average-balance/")
        assert response.status_code == 200
        assert response.data["average_balance"] == Decimal("78734.00")

    def test_number_of_accounts_per_branch(self, accounts):
        response = self.client.get("/account/accounts-count-per-branch/")
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["count"] == 4
        assert response.data[0]["id"] == 1
        assert response.data[0]["branch_name"] == "Main Branch"

    def test_maximum_balance_per_account_type(self, accounts):
        response = self.client.get("/account/maximum-balance-per-account-type/")
        assert response.status_code == 200
        assert "balance" in response.data.keys()
        assert len(response.data["balance"]) == 3
        assert list(response.data["balance"].keys()) == [
            "fixed",
            "salary",
            "savings",
        ]
        assert response.data["balance"]["fixed"] == Decimal(13456.00)
        assert response.data["balance"]["salary"] == Decimal(13456.00)
        assert response.data["balance"]["savings"] == Decimal(274568.00)
