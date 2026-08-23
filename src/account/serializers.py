from rest_framework import serializers


class AccountsCountByStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    count = serializers.IntegerField()


class AccountsCountByAccountTypeSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=20)
    count = serializers.IntegerField()


class TotalAvailableBalanceByAccountTypeSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=20, decimal_places=2)


class TotalNumberOfAccountsOpenedSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class AverageBalanceSerializer(serializers.Serializer):
    average_balance = serializers.IntegerField()


class AccountsCountPerBranchSerializer(TotalNumberOfAccountsOpenedSerializer):
    id = serializers.IntegerField()
    branch_name = serializers.CharField()


class MaximumBalancePerAccountTypeView(TotalNumberOfAccountsOpenedSerializer):
    pass
