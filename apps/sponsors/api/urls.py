from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.sponsors.api.v1.urls'))
]
