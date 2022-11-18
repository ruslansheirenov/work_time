# from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


from .models import User
from .serializers import UserSerializer, UserDetailSerializer

# Create your views here.

class UserListAPIView(ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['organization']
    search_fields = ['first_name', 'last_name', 'email']

class UserDetailAPIView(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

