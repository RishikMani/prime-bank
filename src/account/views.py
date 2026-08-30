from decimal import ROUND_HALF_UP, Decimal

from django.db.models import Avg, Count, Max, Sum
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from branch.models import Branch

from .models import Account
from .serializers import (
    AccountsCountByAccountTypeSerializer,
    AccountsCountByStatusSerializer,
    AccountsCountPerBranchSerializer,
    AverageBalanceSerializer,
    MaximumBalancePerAccountTypeSerializer,
    TotalAvailableBalanceByAccountTypeSerializer,
    TotalNumberOfAccountsOpenedSerializer,
)


class AccountsCountByStatusView(GenericAPIView):
    """Get the total number of accounts based on the their current status.

    e.g. Active -> 80707, Dormant -> 9526, Closed -> 4767
    """

    serializer_class = AccountsCountByStatusSerializer

    def get(self, request, *args, **kwargs):
        rows = (
            Account.objects.all()
            .values("status")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        counts = {row["status"]: row["count"] for row in rows}
        return Response({"counts": counts})


class AccountsCountByAccountTypeView(GenericAPIView):
    """Get the total number of accounts for different account types.

    e.g. Savings -> 47557, Current -> 19021
    """

    serializer_class = AccountsCountByAccountTypeSerializer

    def get(self, request):
        rows = (
            Account.objects.all()
            .values("type")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        counts = {row["type"]: row["count"] for row in rows}
        return Response({"counts": counts})


class TotalAvailableBalanceByAccountTypeView(GenericAPIView):
    """Get the total amount of balance for all account types combined.

    e.g. Savings -> 2187486599.91, Salary -> 644917483.55
    """

    serializer_class = TotalAvailableBalanceByAccountTypeSerializer

    def get(self, request):
        rows = (
            Account.objects.all()
            .values("type")
            .annotate(balance=Sum("balance"))
            .order_by("-balance")
        )

        balance = {row["type"]: row["balance"] for row in rows}

        return Response({"balance": balance})


class TotalNumberOfAccountsOpenedView(GenericAPIView):
    """Get total number of accounts opened."""

    serializer_class = TotalNumberOfAccountsOpenedSerializer

    def get(self, request):
        return Response({"total_number_of_accounts": Account.objects.count()})


class AverageBalanceView(GenericAPIView):
    """Get the average balance across all accounts."""

    serializer_class = AverageBalanceSerializer

    def get(self, request):
        average_balance = Account.objects.aggregate(
            average_balance=Avg("balance")
        )["average_balance"]

        if average_balance is not None:
            # quantize rounds a Decimal to the precision of another Decimal.
            average_balance = average_balance.quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP,
            )
        return Response({"average_balance": average_balance})


class AccountsCountPerBranchView(ListAPIView):
    """Get the number of accounts opened in any branch.

    e.g. Jaipur Branch 6 -> 700, Chandigarh Branch 6 -> 682
    """

    serializer_class = AccountsCountPerBranchSerializer

    def get_queryset(self):
        return (
            Branch.objects.values("id", "branch_name")
            .annotate(count=Count("accounts"))
            .order_by("-count")
        )


class MaximumBalancePerAccountTypeView(GenericAPIView):
    """Get the maximum balance per account type.

    e.g. Current -> 456730.82, Fixed Deposit -> 539198.59
    """

    serializer_class = MaximumBalancePerAccountTypeSerializer

    def get(self, request):
        rows = (
            Account.objects.values("type")
            .annotate(balance=Max("balance"))
            .order_by("type")
        )

        balance = {row["type"]: row["balance"] for row in rows}
        return Response({"balance": balance})
