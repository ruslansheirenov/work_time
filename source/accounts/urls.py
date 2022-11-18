from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserListAPIView)
router.register(r'users', UserDetailAPIView)

urlpatterns = router.urls