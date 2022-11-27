from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.university.api.v1.urls')),
]
