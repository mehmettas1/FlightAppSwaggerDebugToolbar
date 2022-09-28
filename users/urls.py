from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
