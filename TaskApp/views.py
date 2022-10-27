from rest_framework import viewsets
# from imageapp.models import GetImage
from .models import  User
from .serializers import  UserSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer