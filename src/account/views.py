from django.db.models import Avg, Count, Max, Sum
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from branch.models import Branch

from .models import Account
from .serializers import (
    AccountCountByAccountTypeSerializer,
    AccountCountByStatusSerializer,
    AccountsCountPerBranchSerializer,
    AverageBalanceSerializer,
    MaximumAccountPerAccountTypeSerializer,
    TotalAccountBalanceByAccountTypeSerializer,
    TotalAccountsCountSerializer,
)


# Create your views here.
class AccountCountByStatusView(ListAPIView):
    """Get the total number of accounts based on the their current status

    e.g. Active -> 80707, Dormant -> 9526, Closed -> 4767
    """

    serializer_class = AccountCountByStatusSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("status")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class AccountCountByAccountTypeView(ListAPIView):
    """Get the total number of accounts opened for different account types

    e.g. Savings -> 47557, Current -> 19021
    """

    serializer_class = AccountCountByAccountTypeSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("type")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class TotalAccountBalanceByAccountTypeView(ListAPIView):
    """Get the amount of balance for different account types

    e.g. Savings -> 2187486599.91, Salary -> 644917483.55
    """

    serializer_class = TotalAccountBalanceByAccountTypeSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("type")
            .annotate(balance=Sum("balance"))
            .order_by("-balance")
        )


class TotalAccountsCountView(GenericAPIView):
    """Get total number of accounts opened"""

    serializer_class = TotalAccountsCountSerializer

    def get(self, request):
        return Response({"total_number_of_accounts": Account.objects.count()})


class AverageBalanceView(GenericAPIView):
    """Get the average balance across all accounts"""

    serializer_class = AverageBalanceSerializer

    def get(self, request):
        average_balance = Account.objects.aggregate(
            average_balance=Avg("balance")
        )
        return Response({"average_balance": average_balance["average_balance"]})


class AccountsCountPerBranchView(ListAPIView):
    """Get the number of accounts opened in any branch

    e.g. Jaipur Branch 6 -> 700, Chandigarh Branch 6 -> 682
    """

    serializer_class = AccountsCountPerBranchSerializer

    def get_queryset(self):
        return (
            Branch.objects.values("id", "branch_name")
            .annotate(count=Count("accounts"))
            .order_by("-count")
        )


class MaximumBalancePerAccountTypeView(ListAPIView):
    """Get the maximum balance per account type

    e.g. Current -> 456730.82, Fixed Deposit -> 539198.59
    """

    serializer_class = MaximumAccountPerAccountTypeSerializer

    def get_queryset(self):
        return (
            Account.objects.values("type")
            .annotate(balance=Max("balance"))
            .order_by("type")
        )
