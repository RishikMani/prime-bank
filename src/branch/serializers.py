from rest_framework import serializers

from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["id"]


class BranchCountSerializer(serializers.Serializer):
    city = serializers.CharField()
    count = serializers.IntegerField()
