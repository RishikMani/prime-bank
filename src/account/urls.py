from django.urls import path

from .views import (
    AccountCountByAccountTypeView,
    AccountCountByStatusView,
    AccountsCountPerBranchView,
    AverageBalanceView,
    TotalAccountBalanceByAccountTypeView,
    TotalAccountsCountView,
)


urlpatterns = [
    path(
        "count-by-status/",
        AccountCountByStatusView.as_view(),
        name="count_by_status",
    ),
    path(
        "count-by-account-type/",
        AccountCountByAccountTypeView.as_view(),
        name="count_by_account_type",
    ),
    path(
        "total-balance-per-account-type/",
        TotalAccountBalanceByAccountTypeView.as_view(),
        name="total_balance_per_account_type",
    ),
    path(
        "total-number-of-accounts/",
        TotalAccountsCountView.as_view(),
        name="total-number-of-accounts",
    ),
    path(
        "average-balance/", AverageBalanceView.as_view(), name="average-balance"
    ),
    path(
        "accounts-count-per-branch/",
        AccountsCountPerBranchView.as_view(),
        name="accounts-count-per-branch",
    ),
]
