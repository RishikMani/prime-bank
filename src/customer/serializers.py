from rest_framework import serializers

from .models import Customer


class AllCustomersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["id"]


class CustomerCountPerGenderSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=20)
    count = serializers.IntegerField()


class GetAllCustomersFromAStateSerializer(AllCustomersListSerializer):
    pass


class CustomerWithLowestCreditScoreSerializer(AllCustomersListSerializer):
    pass


class CustomerWithHighestCreditScoreSerializer(AllCustomersListSerializer):
    pass


class CustomersWithinCreditScoreRangeSerializer(AllCustomersListSerializer):
    pass


class CustomerWithLowestAnnualIncomeSerializer(AllCustomersListSerializer):
    pass


class CustomerWithHighestAnnualIncomeSerializer(AllCustomersListSerializer):
    pass


class CustomersBelowAnnualIncomeSerializer(AllCustomersListSerializer):
    pass
