from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.accounts.api.v1.permissions import IsOwnUserOrReadOnly
from apps.donate.models import Donate
from .serializers import DonateSerializer


class DonateListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/donate/api/v1/list/
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)


class DonateRetrieveAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/donate/api/v1/retrieve/<int:pk>/
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)


class DonateCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/donate/api/v1/create/
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

