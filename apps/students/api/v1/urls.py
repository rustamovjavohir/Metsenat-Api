from django.urls import path

from .views import StudentWalletListAPIView, StudentRetrieveAPIView

urlpatterns = [
    path('list/', StudentWalletListAPIView.as_view()),
    path('retrieve/<int:pk>/', StudentRetrieveAPIView.as_view()),
]
