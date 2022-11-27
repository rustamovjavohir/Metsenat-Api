from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.accounts.api.v1.urls'))
]