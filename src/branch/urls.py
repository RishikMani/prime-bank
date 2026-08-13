from django.urls import path

from .views import (
    BranchCountByCityView,
    BranchCountByStateView,
    BranchCountPerCityView,
    BranchCountPerStateView,
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
        "branch-count-city/<str:city>/",
        BranchCountByCityView.as_view(),
        name="branch_count_by_city",
    ),
    path(
        "branch-count-per-city/",
        BranchCountPerCityView.as_view(),
        name="branch_count_per_city",
    ),
    path(
        "branch-count-state/<str:state>/",
        BranchCountByStateView.as_view(),
        name="branch_count_by_city",
    ),
    path(
        "branch-count-per-state/",
        BranchCountPerStateView.as_view(),
        name="branch_count_per_state",
    ),
]
