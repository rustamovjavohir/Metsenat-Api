from django.urls import path

from .views import AccountRegisterAPIView, AccountListAPIView, MyAccountAPIView, LoginAPIView, AccountOwnImageUpdateView

urlpatterns = [
    path('register/', AccountRegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profiles/', AccountListAPIView.as_view()),
    path('profile/<str:phone>/', MyAccountAPIView.as_view()),
    path('image-update/<int:pk>/', AccountOwnImageUpdateView.as_view()),
]
