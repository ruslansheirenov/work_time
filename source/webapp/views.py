import qrcode
from django.http import FileResponse
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Organization, OrganizationWorkTime, WorkTime
from .serializers import OrganizationSerializer, OrganizationWorkTimeSerializer, WorkTimeSerializer

# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationWorkTimeViewSet(viewsets.ModelViewSet):
    queryset = OrganizationWorkTime.objects.all()
    serializer_class = OrganizationWorkTimeSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_time']


class QRCodeAPIView(APIView):
    def get(self, request, pk):
        data = f'http://127.0.0.1/api/v1/organizations/{pk}'
        filename = f'qrcode_{pk}.png'
        path = f'storage/{filename}'

        qr_img = qrcode.make(data)
        qr_img.save(path)

        return FileResponse(open(path, 'rb'))