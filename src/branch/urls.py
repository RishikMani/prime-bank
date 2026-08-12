from django.urls import path

from .views import ListBranches


urlpatterns = [path("branches/", ListBranches.as_view(), name="branch_list")]
