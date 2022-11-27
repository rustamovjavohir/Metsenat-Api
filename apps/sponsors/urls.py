from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.sponsors.api.urls'))
]
