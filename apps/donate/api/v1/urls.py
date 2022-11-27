from django.urls import path

from .views import DonateListAPIView, DonateRetrieveAPIView, DonateCreateAPIView

urlpatterns = [
    path('list/', DonateListAPIView.as_view()),
    path('retrieve/<int:pk>/', DonateRetrieveAPIView.as_view()),
    path('create/', DonateCreateAPIView.as_view())
]
