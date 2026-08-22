from rest_framework import serializers


class AccountCountByStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    count = serializers.IntegerField()


class AccountCountByAccountTypeSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=20)
    count = serializers.IntegerField()


class TotalAccountBalanceByAccountTypeSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=20, decimal_places=2)


class TotalAccountsCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class AverageBalanceSerializer(serializers.Serializer):
    average_balance = serializers.IntegerField()


class AccountsCountPerBranchSerializer(TotalAccountsCountSerializer):
    id = serializers.IntegerField()
    branch_name = serializers.CharField()


class MaximumAccountPerAccountTypeSerializer(
    TotalAccountBalanceByAccountTypeSerializer
):
    pass
