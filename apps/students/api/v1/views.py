from rest_framework import generics

from apps.students.models import StudentWallet
from .serializers import StudentWalletSerializer


class StudentWalletListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/students/api/v1/list/
    queryset = StudentWallet.objects.all()
    serializer_class = StudentWalletSerializer


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/students/api/v1/retrieve/<int:pk>/
    queryset = StudentWallet.objects.all()
    serializer_class = StudentWalletSerializer
