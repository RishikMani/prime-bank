from django.db.models import Count, Q
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Customer
from .serializers import (
    AllCustomersListSerializer,
    CustomerCountPerGenderSerializer,
    CustomerCountPerStateSerializer,
    CustomersAboveAnnualIncomeSerializer,
    CustomersBelowAnnualIncomeSerializer,
    CustomersWithinAnnualIncomeRangeSerializer,
    CustomersWithinCreditScoreRangeSerializer,
    CustomerWithHighestAnnualIncomeSerializer,
    CustomerWithHighestCreditScoreSerializer,
    CustomerWithLowestAnnualIncomeSerializer,
    CustomerWithLowestCreditScoreSerializer,
    GetAllCustomersFromAStateSerializer,
)


class CustomerPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class AllCustomersListView(ListAPIView):
    serializer_class = AllCustomersListSerializer
    pagination_class = CustomerPagination

    def get_queryset(self):
        return Customer.objects.all()


class CustomerCountPerGenderView(GenericAPIView):
    serializer_class = CustomerCountPerGenderSerializer

    def get(self, request):
        rows = (
            Customer.objects.values("gender")
            .annotate(count=Count("gender"))
            .order_by("-count")
        )

        gender = {row["gender"]: row["count"] for row in rows}
        return Response({"gender": gender})


class GetAllCustomersFromAStateView(ListAPIView):
    serializer_class = GetAllCustomersFromAStateSerializer
    pagination_class = CustomerPagination

    def get_queryset(self):
        state = self.kwargs["state"]

        # TODO: give correct error when non-existing state provided
        if state not in Customer.StateChoices.values:
            print("wrong state chosen")

        return Customer.objects.filter(Q(state__icontains=state))


class CustomerCountPerStateView(GenericAPIView):
    serializer_class = CustomerCountPerStateSerializer

    def get(self, request):
        rows = (
            Customer.objects.values("state")
            .annotate(count=Count("state"))
            .order_by("state")
        )

        state = {row["state"]: row["count"] for row in rows}

        return Response({"customers_per_state": state})


class CustomerWithLowestCreditScoreView(GenericAPIView):
    serializer_class = CustomerWithLowestCreditScoreSerializer

    def get(self, request):
        customer = Customer.objects.order_by("credit_score").first()
        serializer = self.get_serializer(customer)
        return Response({"customer": serializer.data})


class CustomerWithHighestCreditScoreView(GenericAPIView):
    serializer_class = CustomerWithHighestCreditScoreSerializer

    def get(self, request):
        customer = Customer.objects.order_by("-credit_score").first()
        serializer = self.get_serializer(customer)
        return Response({"customer": serializer.data})


class CustomersWithinCreditScoreRangeView(ListAPIView):
    serializer_class = CustomersWithinCreditScoreRangeSerializer
    pagination_class = CustomerPagination
    pagination_class.page_size = 1000

    def get_queryset(self):
        min_credit_score = self.request.query_params["min_score"]
        max_credit_score = self.request.query_params["max_score"]

        # TODO: what if both are empty
        if min_credit_score and max_credit_score:
            customers = Customer.objects.filter(
                credit_score__gte=min_credit_score,
                credit_score__lte=max_credit_score,
            )
        elif min_credit_score and not max_credit_score:
            customers = Customer.objects.filter(
                credit_score__gte=min_credit_score
            )
        else:
            customers = Customer.objects.filter(
                credit_score__lte=max_credit_score
            )

        return customers.order_by("credit_score")


class CustomerWithLowestAnnualIncomeView(GenericAPIView):
    serializer_class = CustomerWithLowestAnnualIncomeSerializer

    def get(self, request):
        customer = Customer.objects.order_by("income").first()
        serializer = self.get_serializer(customer)
        return Response({"customer": serializer.data})


class CustomerWithHighestAnnualIncomeView(GenericAPIView):
    serializer_class = CustomerWithHighestAnnualIncomeSerializer

    def get(self, request):
        customer = Customer.objects.order_by("-income").first()
        serializer = self.get_serializer(customer)
        return Response({"customer": serializer.data})


class CustomersBelowAnnualIncomeView(ListAPIView):
    serializer_class = CustomersBelowAnnualIncomeSerializer
    pagination_class = CustomerPagination

    def get_queryset(self):
        annual_income = self.kwargs["annual_income"]
        customers = Customer.objects.filter(income__lte=annual_income).order_by(
            "income"
        )
        return customers


class CustomersAboveAnnualIncomeView(ListAPIView):
    serializer_class = CustomersAboveAnnualIncomeSerializer
    pagination_class = CustomerPagination

    def get_queryset(self):
        annual_income = self.kwargs["annual_income"]
        customers = Customer.objects.filter(income__gte=annual_income).order_by(
            "income"
        )
        return customers


class CustomersWithinAnnualIncomeRangeView(ListAPIView):
    serializer_class = CustomersWithinAnnualIncomeRangeSerializer
    pagination_class = CustomerPagination
    pagination_class.page_size = 200

    def get_queryset(self):
        min_income = self.request.query_params["min_income"]
        max_income = self.request.query_params["max_income"]

        # TODO: what if both are empty
        if min_income and max_income:
            customers = Customer.objects.filter(
                income__gte=min_income,
                income__lte=max_income,
            )
        elif min_income and not max_income:
            customers = Customer.objects.filter(income__gte=min_income)
        else:
            customers = Customer.objects.filter(income__lte=max_income)

        return customers.order_by("income")
