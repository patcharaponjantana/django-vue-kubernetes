from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('location', views.LocationViewSet)
router.register('ferry_type', views.FerryTypeViewSet)
router.register('boat-schedule', views.BoatScheduleViewSet)
router.register('booking', views.BookingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]