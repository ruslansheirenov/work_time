from rest_framework import serializers

from .models import User
from webapp.serializers import OrganizationSerializer, WorkTimeMonthSerializer

class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'organization', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    worked_time = WorkTimeMonthSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'worked_time')