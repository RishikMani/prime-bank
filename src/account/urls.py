from django.urls import path

from .views import (
    AccountCountByAccountTypeView,
    AccountCountByStatusView,
    AccountsCountPerBranchView,
    AverageBalanceView,
    MaximumBalancePerAccountTypeView,
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
        name="total_number_of_accounts",
    ),
    path(
        "average-balance/", AverageBalanceView.as_view(), name="average_balance"
    ),
    path(
        "accounts-count-per-branch/",
        AccountsCountPerBranchView.as_view(),
        name="accounts-count-per-branch",
    ),
    path(
        "maximum-balance-per-account-type/",
        MaximumBalancePerAccountTypeView.as_view(),
        name="maximum_balance_per_account_type",
    ),
]
