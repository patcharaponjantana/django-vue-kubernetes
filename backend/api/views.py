from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers, filters

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# App
class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class FerryTypeViewSet(viewsets.ModelViewSet):
    queryset = models.FerryType.objects.all()
    serializer_class = serializers.FerryTypeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

class BoatScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.BoatSchedule.objects.all()
    serializer_class = serializers.BoatScheduleSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.BoatScheduleFilter

    # def get_permissions(self):
    #     if self.request.method in ['GET']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.IsAdminUser()]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
