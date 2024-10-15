from django.shortcuts import render

# Create your views here.
from utils import custom_viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class BachatGatRegistrationViewSet(custom_viewsets.ModelViewSet):
    model = BachatGatRegistration
    queryset = BachatGatRegistration.objects.all()
    serializer_class = BachatGatRegistrationSerializers
    list_success_message = "list the data success"
    retrieve_sucess_message ="retrieve returend success"
    create_success_message = "bachatgat registration created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg":'success',
        "data": {}
    }

class MemberRegistrationViewSet(custom_viewsets.ModelViewSet):
    model = MemberRegistration
    queryset = MemberRegistration.objects.all()
    serializer_class = MemberRegistrationSerializers
    list_success_message ="list the data "
    create_success_message = "create the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg":'member registration view data featch',
        "data":{} 
    }

class BankDetailViewSet(custom_viewsets.ModelViewSet):
    model = BankDetail
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializers
    list_success_message = "bank detail in the list success"
    retrieve_sucess_message ="retrieve returend success"
    create_success_message = "bank details created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'bank detail view data featch',
        "data": {}
    }


class MeetingViewSet(custom_viewsets.ModelViewSet):
    model = Meeting
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializers
    list_success_message = 'meeting data list success'
    create_success_message = 'created meeting data success '
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg":'meeting view data featch ',
        "data":{}
    }

class UserDetailViewSet(custom_viewsets.ModelViewSet):
    model = UserDetail
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializers
    list_success_message = "user list the data success"
    retrieve_sucess_message ="retrieve returend success"
    create_success_message = "user created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status":200,
        "msg": 'user detail success',
        "data": {}
    }

class SavingsViewSet(custom_viewsets.ModelViewSet):
    model = Savings
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializers
    list_success_message = 'saving data list success'
    create_success_message = 'created the data success'
    satus_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'saving detail successfully',
        "data": {}
    }

class LoanViewSet(custom_viewsets.ModelViewSet):
    model = Loan
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers
    list_success_message = 'data in list success'
    create_success_message = 'creted the data success'
    satus_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'loan data view featch',
        "data": {}
    }

class FundDistributionViewSet(custom_viewsets.ModelViewSet):
    model = FundDistribution
    queryset = FundDistribution.objects.all()
    serializer_class = FundDistributionSerializers
    list_success_message = 'data of list success'
    create_success_message = 'created the data'
    satus_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'fund distribution data success',
        "data": {}
    }

class AttendanceViewSet(custom_viewsets.ModelViewSet):
    model = Attendance
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers
    list_success_message = 'attendance data list success'
    create_success_message = 'created attendance data success '
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg":'attendance view data featch ',
        "data":{}
    }

class ReportsViewSet(custom_viewsets.ModelViewSet):
    model = Reports
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializers
    list_success_message = 'reports data list success'
    create_success_message = 'created reports data success '
    status_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg":'report view data featch ',
        "data":{}
    }
