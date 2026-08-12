from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Branch
from .serializers import BranchSerializer


class ListBranches(APIView):
    """
    View to list all bank branches.
    """

    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
