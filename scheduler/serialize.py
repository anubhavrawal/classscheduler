from rest_framework import serializers
from .models import Rooms, fields

class Roomsserializer(serializers.ModelSerializer):
    class Meta:
        model=Rooms
        fields='__all__'