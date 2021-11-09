from django.urls import path
from django.urls import include, path
from django.contrib.auth.models import User
from . import views
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', views.main_page, name='scheduler-home'),
    path('', include(router.urls)),
    path('rooms', views.room_page, name='scheduler-rooms'),
    path('instructors', views.instructor_page, name='scheduler-instructors'),
    path('api-post', include('rest_framework.urls'))
]
