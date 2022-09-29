from rest_framework import routers
from .views import FlightView


router = routers.DefaultRouter()
router.register('flights', FlightView)

urlpatterns = [
    
]

urlpatterns += router.urls