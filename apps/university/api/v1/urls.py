from django.urls import path
from .views import OTMListAPIView

urlpatterns = [
    path('list/', OTMListAPIView.as_view()),
]
