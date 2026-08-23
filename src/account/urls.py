from django.urls import path

from .views import (
    AccountsCountByAccountTypeView,
    AccountsCountByStatusView,
    AccountsCountPerBranchView,
    AverageBalanceView,
    MaximumBalancePerAccountTypeView,
    TotalAvailableBalanceByAccountTypeView,
    TotalNumberOfAccountsOpenedView,
)


urlpatterns = [
    path(
        "count-by-status/",
        AccountsCountByStatusView.as_view(),
        name="count_by_status",
    ),
    path(
        "count-by-account-type/",
        AccountsCountByAccountTypeView.as_view(),
        name="count_by_account_type",
    ),
    path(
        "total-balance-per-account-type/",
        TotalAvailableBalanceByAccountTypeView.as_view(),
        name="total_balance_per_account_type",
    ),
    path(
        "total-number-of-accounts/",
        TotalNumberOfAccountsOpenedView.as_view(),
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
