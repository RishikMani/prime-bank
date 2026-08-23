import pytest

from django.db.utils import DataError

from base import settings
from branch.models import Branch


# update the HOST in Django settingsto point to localhost
settings.DATABASES["default"]["HOST"] = "localhost"


@pytest.mark.django_db
class TestModel:
    @pytest.mark.django_db(transaction=True)
    def test_create_branch_with_name_with_more_than_50_characters(self):
        with pytest.raises(DataError):
            Branch.objects.create(
                id=1,
                branch_name="This branch name is bigger than 50 characters to break it",
                city="Mumbai",
                state="Maharashtra",
                opening_date="2020-01-01",
                ifsc="ABCD0123456",
            )

    @pytest.mark.django_db(transaction=True)
    def test_create_branch_with_city_with_more_than_50_characters(self):
        with pytest.raises(DataError):
            Branch.objects.create(
                id=1,
                branch_name="Main branch",
                city="The city name is bigger than 50 characters to break it",
                state="Maharashtra",
                opening_date="2020-01-01",
                ifsc="ABCD0123456",
            )

    @pytest.mark.django_db(transaction=True)
    def test_create_branch_with_state_with_more_than_50_characters(self):
        with pytest.raises(DataError):
            Branch.objects.create(
                id=1,
                branch_name="Main branch",
                city="Mumbai",
                state="The state name is bigger than 50 characters to break it",
                opening_date="2020-01-01",
                ifsc="ABCD0123456",
            )

    @pytest.mark.django_db(transaction=True)
    def test_create_branch_with_ifsc_with_more_than_12_characters(self):
        with pytest.raises(DataError):
            Branch.objects.create(
                id=1,
                branch_name="Main branch",
                city="Mumbai",
                state="Maharashtra",
                opening_date="2020-01-01",
                ifsc="ABCD012345678",
            )

    def test_branch_is_active_by_default(self):
        Branch.objects.create(
            id=1,
            branch_name="Main Branch",
            city="Mumbai",
            state="Maharashtra",
            opening_date="2020-01-01",
            ifsc="ABCD0123456",
        )
        assert Branch.objects.get(pk=1).is_active
