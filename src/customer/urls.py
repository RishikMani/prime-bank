from django.urls import path

from .views import (
    AllCustomersListView,
    CustomerCountPerGenderView,
    CustomerCountPerStateView,
    CustomersAboveAnnualIncomeView,
    CustomersBelowAnnualIncomeView,
    CustomersWithinAnnualIncomeRangeView,
    CustomersWithinCreditScoreRangeView,
    CustomerWithHighestAnnualIncomeView,
    CustomerWithHighestCreditScoreView,
    CustomerWithLowestAnnualIncomeView,
    CustomerWithLowestCreditScoreView,
    GetAllCustomersFromAStateView,
)


urlpatterns = [
    path("", AllCustomersListView.as_view(), name="list-all-customers"),
    path(
        "customer-count--per-gender/",
        CustomerCountPerGenderView.as_view(),
        name="customer-count-per-gender",
    ),
    path(
        "all-customers-in-a-state/<str:state>/",
        GetAllCustomersFromAStateView.as_view(),
        name="list-all-customers-in-a-state",
    ),
    path(
        "customer-count-per-state/",
        CustomerCountPerStateView.as_view(),
        name="customer-count-per-state",
    ),
    path(
        "customer-with-lowest-credit-score/",
        CustomerWithLowestCreditScoreView.as_view(),
        name="customer-with-lowest-credit-score",
    ),
    path(
        "customer-with-highest-credit-score/",
        CustomerWithHighestCreditScoreView.as_view(),
        name="customer-with-highest-credit-score",
    ),
    path(
        "customers-within-credit-score-range/",
        CustomersWithinCreditScoreRangeView.as_view(),
        name="customers-within-credit-score-range",
    ),
    path(
        "customer-with-lowest-annual-income/",
        CustomerWithLowestAnnualIncomeView.as_view(),
        name="customer-with-lowest-annual-income",
    ),
    path(
        "customer-with-highest-annual-income/",
        CustomerWithHighestAnnualIncomeView.as_view(),
        name="customer-with-highest-annual-income",
    ),
    path(
        "customers-below-annual-income/<int:annual_income>/",
        CustomersBelowAnnualIncomeView.as_view(),
        name="customers-below-annual-income",
    ),
    path(
        "customers-above-annual-income/<int:annual_income>/",
        CustomersAboveAnnualIncomeView.as_view(),
        name="customers-above-annual-income",
    ),
    path(
        "customers-within-annual-income-range/",
        CustomersWithinAnnualIncomeRangeView.as_view(),
        name="customers-within-annual-income-range",
    ),
]
