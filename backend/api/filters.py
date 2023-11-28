import django_filters
from . import models

class BoatScheduleFilter(django_filters.FilterSet):
    departure_time__date = django_filters.filters.DateTimeFilter(field_name='departure_time__date', lookup_expr='exact')

    class Meta:
        model = models.BoatSchedule
        fields = {
            'from_location__name': ['exact'],
            'to_location__name': ['exact'],
        }

