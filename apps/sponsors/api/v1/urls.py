from django.urls import path

from .views import SponsorWalletListAPIView, SponsorWalletRetrieveAPIView, SponsorWalletCreateAPIView, SponsorStatistic

urlpatterns = [
    path('create/', SponsorWalletCreateAPIView.as_view()),
    path('list/', SponsorWalletListAPIView.as_view()),
    path('retrieve/<int:pk>/', SponsorWalletRetrieveAPIView.as_view()),
    path('statistic/', SponsorStatistic.as_view())
]
