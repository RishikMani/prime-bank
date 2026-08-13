from django.urls import path

from .views import (
    BranchCountByCityView,
    BranchCountPerCityView,
    BranchListByCityOrStateView,
    BranchListView,
)


urlpatterns = [
    path("", BranchListView.as_view(), name="branch_list"),
    path(
        "branch-by-city-or-state/<str:place>/",
        BranchListByCityOrStateView.as_view(),
        name="branch_by_city_or_state",
    ),
    path(
        "total-branch-count-by-city/<str:city>/",
        BranchCountByCityView.as_view(),
        name="branch_count_by_city",
    ),
    path(
        "total-branch-count-per-city/",
        BranchCountPerCityView.as_view(),
        name="branch_count_per_city",
    ),
]
