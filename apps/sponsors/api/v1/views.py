from django.db.models import Count, Sum, Avg
from django.db.models.functions import TruncMonth
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.models import Account
from apps.donate.models import Donate
from apps.students.models import StudentWallet
from apps.accounts.api.v1.permissions import IsOwnUserOrReadOnly
from apps.sponsors.models import SponsorWallet
from .serializers import SponsorWalletSerializer, SponsorCreateSerializer


class SponsorWalletCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/sponsors/api/v1/create/
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorCreateSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SponsorWalletListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/sponsors/api/v1/list/
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorWalletSerializer


class SponsorWalletRetrieveAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/sponsors/api/v1/retrieve/<int:pk>//
    queryset = SponsorWallet.objects.all()
    serializer_class = SponsorWalletSerializer


class SponsorStatistic(APIView):
    # http://127.0.0.1:8000/sponsors/api/v1/statistic/
    permission_classes = (IsAdminUser, )
    def get(self, *args, **kwargs):
        data = {}
        queryset = Account.objects.filter(is_sponsor=True).annotate(day=TruncMonth('date_created')).values('day').annotate(count=Count('id'))

        for i in queryset:
            data[str(i.get('day').date())] = i.get('count')
        # return Response(data)
        # aggregate
        total_amount_paid = Donate.objects.aggregate(summa=Sum("donate"))
        total_amount_process = SponsorWallet.objects.filter(status=1).aggregate(summa=Sum('spent_amount'))

        total_amount_payable = StudentWallet.objects.aggregate(summa=Sum('contract_amount'))
        data['Total amount paid'] = total_amount_paid
        data['Total amount process'] = total_amount_process
        data['Total amount payable'] = total_amount_payable

        print(total_amount_process)
        return Response(data)


