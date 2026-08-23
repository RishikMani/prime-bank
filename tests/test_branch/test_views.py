import pytest

from rest_framework.test import APIClient

from base import settings
from branch.models import Branch


# update the HOST in Django settingsto point to localhost
settings.DATABASES["default"]["HOST"] = "localhost"


@pytest.fixture
def branches():
    return Branch.objects.bulk_create(
        [
            Branch(
                id=1,
                branch_name="Main Branch",
                city="Mumbai",
                state="Maharashtra",
                opening_date="2020-01-01",
                ifsc="ABCD0123456",
            ),
            Branch(
                id=2,
                branch_name="Central Branch",
                city="Delhi",
                state="Delhi",
                opening_date="2021-06-15",
                ifsc="EFGH0123456",
            ),
        ]
    )


@pytest.mark.django_db
class TestBranchListView:
    client = APIClient()

    def test_get_all_branches_as_list(self, branches):
        response = self.client.get("/branch/")
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert len(response.data) == 2, "Exactly 2 records must exist"
