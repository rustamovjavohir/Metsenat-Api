from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.donate.api.v1.urls'))
]
