from django.db.models import Avg, Count, Sum
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from branch.models import Branch

from .models import Account
from .serializers import (
    AccountCountByAccountTypeSerializer,
    AccountCountByStatusSerializer,
    AccountsCountPerBranchSerializer,
    AverageBalanceSerializer,
    TotalAccountBalanceByAccountTypeSerializer,
    TotalAccountsCountSerializer,
)


# Create your views here.
class AccountCountByStatusView(ListAPIView):
    serializer_class = AccountCountByStatusSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("status")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class AccountCountByAccountTypeView(ListAPIView):
    serializer_class = AccountCountByAccountTypeSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("type")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class TotalAccountBalanceByAccountTypeView(ListAPIView):
    serializer_class = TotalAccountBalanceByAccountTypeSerializer

    def get_queryset(self):
        return (
            Account.objects.all()
            .values("type")
            .annotate(balance=Sum("balance"))
            .order_by("-balance")
        )


class TotalAccountsCountView(GenericAPIView):
    serializer_class = TotalAccountsCountSerializer

    def get(self, request):
        return Response({"total_number_of_accounts": Account.objects.count()})


class AverageBalanceView(GenericAPIView):
    serializer_class = AverageBalanceSerializer

    def get(self, request):
        average_balance = Account.objects.aggregate(
            average_balance=Avg("balance")
        )
        return Response({"average_balance": average_balance["average_balance"]})


class AccountsCountPerBranchView(ListAPIView):
    serializer_class = AccountsCountPerBranchSerializer

    def get_queryset(self):
        return (
            Branch.objects.values("id", "branch_name")
            .annotate(count=Count("accounts"))
            .order_by("-count")
        )
