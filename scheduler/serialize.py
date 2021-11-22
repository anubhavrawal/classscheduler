from rest_framework import serializers
from .models import Rooms, fields

class Roomsserializer(serializers.Serializer):
    campus = serializers.CharField()
    building = serializers.CharField()
    room_num = serializers.CharField()
    capacity = serializers.IntegerField(max_value=2147483647, min_value=-2147483648)
    room_type = serializers.CharField(max_length=3)
    '''
    class Meta:
        model=Rooms
        fields='__all__'
    '''  
    
    def create(self, validated_data):
        return Rooms.objects.create(**validated_data)