from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Branch
from .serializers import BranchCountSerializer, BranchSerializer


class BranchListView(APIView):
    """View to list all the bank branches"""

    def get(self, request, **kwargs):
        branches = self.get_queryset()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Branch.objects.all()


class BranchListByCityOrStateView(BranchListView):
    """List all the branches in cities or state based on place provided"""

    def get_queryset(self):
        place = self.kwargs["place"]
        return Branch.objects.filter(
            Q(city__icontains=place) | Q(state__icontains=place)
        )


class BranchCountByCityView(APIView):
    """Returns the branch count provided a city name"""

    def get(self, request, **kwargs):
        branches = self.get_queryset()
        serializer = BranchCountSerializer(branches, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        city = self.kwargs["city"]
        return (
            Branch.objects.filter(Q(city__icontains=city))
            .values("city")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class BranchCountPerCityView(APIView):
    """Returns the branch count of all the cities"""

    def get(self, request):
        branches = (
            Branch.objects.all()
            .values("city")
            .annotate(count=Count("id"))
            .order_by("-count")
        )
        serializer = BranchCountSerializer(branches, many=True)
        return Response(serializer.data)
