from rest_framework import serializers

from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["id"]


class BranchCountByCitySerializer(serializers.Serializer):
    city = serializers.CharField()
    count = serializers.IntegerField()


class BranchCountPerCitySerializer(BranchCountByCitySerializer):
    pass


class BranchCountByStateSerializer(serializers.Serializer):
    state = serializers.CharField()
    count = serializers.IntegerField()


class BranchCountPerStateSerializer(BranchCountByStateSerializer):
    pass
