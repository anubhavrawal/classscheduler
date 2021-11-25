from rest_framework import serializers
from .models import Rooms, fields, Instructors
from .forms import UpdateForm
from rest_framework.response import Response
from rest_framework import status


#-----------------------Instructor Searilizer------------------------------------------
class InstructorListserializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Instructors(**item) for item in validated_data]
        return Instructors.objects.bulk_create(books)

    def update(self, instance, validated_data):
        updated_instances = [] 
        
        for data in validated_data:
            try:
                instance = Instructors.objects.get(id = data['id'])
                instance.campus = data['last_name']
                instance.building = data['first_name']
                instance.room_num = data['status']
                instance.capacity = data['department']
                instance.save()
            
            except:
                #validated_data.pop('id')
                instance = Instructors.objects.create(**data)
            

            updated_instances.append(instance)
        
        return updated_instances

class Instructorserializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Instructors
        fields=['id','last_name', 'first_name', 'status', 'department']
        list_serializer_class = InstructorListserializer

     
    @classmethod
    def many_init(cls, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = cls()
        # Instantiate the parent list serializer.
        return InstructorListserializer(*args, **kwargs)
     
    
    def create(self, validated_data):
        instance = Instructors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.campus = validated_data.get('last_name', instance.campus)
        instance.building = validated_data.get('first_name', instance.building)
        instance.room_num = validated_data.get('status', instance.room_num)
        instance.capacity = validated_data.get('department', instance.capacity)
        instance.save()

        return instance
    
    def delete(self, request, pk):
        instance = Instructors.objects.get(id = pk)
        instance.delete()
        return Response({"message":"Record "+ instance.room_num +" was sucessfully deleted!!" })
#-----------------------Instructor Searilizer End------------------------------------------





#-----------------------Room Searilizer------------------------------------------
class RoomsListserializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Rooms(**item) for item in validated_data]
        return Rooms.objects.bulk_create(books)

    def update(self, instance, validated_data):
        updated_instances = [] 
        
        for data in validated_data:
            try:
                instance = Rooms.objects.get(id = data['id'])
                instance.campus = data['campus']
                instance.building = data['building']
                instance.room_num = data['room_num']
                instance.capacity = data['capacity']
                instance.room_type = data['room_type']
                instance.save()
            
            except:
                #validated_data.pop('id')
                instance = Rooms.objects.create(**data)
            

            updated_instances.append(instance)
        
        return updated_instances

class Roomsserializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Rooms
        fields=['id','campus', 'building', 'room_num', 'capacity', 'room_type']
        list_serializer_class = RoomsListserializer

     
    @classmethod
    def many_init(cls, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = cls()
        # Instantiate the parent list serializer.
        return RoomsListserializer(*args, **kwargs)
     
    
    def create(self, validated_data):
        isntance = Rooms.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.campus = validated_data.get('campus', instance.campus)
        instance.building = validated_data.get('building', instance.building)
        instance.room_num = validated_data.get('room_num', instance.room_num)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.room_type = validated_data.get('room_type', instance.room_type)
        instance.save()

        return instance
    
    def delete(self, request, pk):
        instance = Rooms.objects.get(id = pk)
        instance.delete()
        return Response({"message":"Record "+ instance.room_num +" was sucessfully deleted!!" })