from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models 

class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# App
# class BookingUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.BookingUser
#         fields = '__all__'

class FerryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FerryType
        fields = '__all__'

class BoatScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoatSchedule
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'