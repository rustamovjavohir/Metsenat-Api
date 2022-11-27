from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.students.api.v1.urls'))
]
