from django.db import models

from worktime.settings import AUTH_USER_MODEL

# Create your models here.

class Organization(models.Model):
    org_name = models.CharField(max_length=100, verbose_name='Organization Name')
    email = models.EmailField(verbose_name='Organization Email')


    def __str__(self) -> str:
        return str(self.org_name)

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organization name'
        verbose_name_plural = 'Organization names'


class OrganizationWorkTime(models.Model):
    org_name = models.ForeignKey(Organization, on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name='Work Start Time')
    end_time = models.TimeField(verbose_name='Work End Time')


    def __str__(self) -> str:
        return str(self.org_name)

    class Meta:
        db_table = 'organizationworktimes'
        verbose_name = 'Organization Work Time'
        verbose_name_plural = 'Organizations Work Times'


class WorkTime(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worked_time')
    organization = models.ForeignKey(Organization, related_name='users_work_time', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Work Start Time')
    end_time = models.DateTimeField(verbose_name='Work End Time')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Work End Time')

    def __str__(self) -> str:
        return str(self.user.first_name)

    class Meta:
        db_table = 'userworktimes'
        verbose_name = 'User Work Time'
        verbose_name_plural = 'Users Work Times'