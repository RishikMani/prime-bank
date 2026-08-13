from django.db.models import Count, Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Branch
from .serializers import (
    BranchCountByCitySerializer,
    BranchCountByStateSerializer,
    BranchCountPerCitySerializer,
    BranchCountPerStateSerializer,
    BranchSerializer,
)


# Leaving this class intentionally subclassing APIView so that I can later
# compare generic views with APIViews.
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


class BranchCountByCityView(ListAPIView):
    """Returns the branch count provided a city name"""

    serializer_class = BranchCountByCitySerializer

    def get_queryset(self):
        city = self.kwargs["city"]

        return (
            Branch.objects.filter(Q(city__icontains=city))
            .values("city")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class BranchCountPerCityView(ListAPIView):
    """Returns the branch count of all the cities"""

    serializer_class = BranchCountPerCitySerializer

    def get_queryset(self):
        return (
            Branch.objects.all()
            .values("city")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class BranchCountByStateView(ListAPIView):
    """Returns the branch count provided a state name"""

    serializer_class = BranchCountByStateSerializer

    def get_queryset(self):
        state = self.kwargs["state"]

        return (
            Branch.objects.filter(Q(state__icontains=state))
            .values("state")
            .annotate(count=Count("id"))
            .order_by("-count")
        )


class BranchCountPerStateView(ListAPIView):
    """Returns the branch count of all the states"""

    serializer_class = BranchCountPerStateSerializer
    queryset = (
        Branch.objects.all()
        .values("state")
        .annotate(count=Count("id"))
        .order_by("-count")
    )
