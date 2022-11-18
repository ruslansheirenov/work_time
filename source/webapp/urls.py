from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r"organizations", OrganizationViewSet)
router.register(r"organizations/worktime", OrganizationWorkTimeViewSet)
router.register(r"users/worktime", WorkTimeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/qrcode/<int:pk>/', QRCodeAPIView.as_view())
]