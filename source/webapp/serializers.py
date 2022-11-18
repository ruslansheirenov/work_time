from rest_framework import serializers
from datetime import datetime, timedelta

from .models import *
from accounts.models import User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'org_name', 'email')


class OrganizationWorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationWorkTime
        fields = ('id', 'org_name', 'start_time', 'end_time')


class WorkTimeMonthSerializer(serializers.Serializer):
    def to_representation(self, data):
        current_month = datetime.now().month
        data2 = {}

        organizations = data.values('organization_id').filter(start_time__month=current_month).distinct()

        for i in organizations:
            org_id = i['organization_id']

            worktime = data.filter(start_time__month=current_month, organization=org_id).values('start_time', 'end_time')

            time = timedelta()

            for a in worktime:
                start_time = datetime.strptime(str(datetime.time(a['start_time'])), '%H:%M:%S')
                end_time = datetime.strptime(str(datetime.time(a['end_time'])), '%H:%M:%S')
                time += end_time - start_time

            data2.update({org_id: time / 3600})

        return data2


class WorkTimeSerializer(serializers.ModelSerializer):
    organization = serializers.SlugRelatedField(read_only=True, slug_field='name')
    start_time = serializers.DateTimeField(format='%H:%M')
    end_time = serializers.DateTimeField(format='%H:%M')

    class Meta:
        model = WorkTime
        fielsd = ('id', 'user', 'users_work_time', 'start_time', 'end_time')
            
    def to_representation(self, instance):
        worked_time = (instance.end_time - instance.start_time) / 3600
        time = super().to_representation(instance)
        time.update(worked_time=worked_time)
        return time