from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils import custom_viewsets
from rest_framework.decorators import *


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
        "msg":'bachatgat registration view data featch',
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
        "msg":'member registration success',
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
        "msg": 'bank detail data view featch',
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
        "msg": 'user detail data view featch successfully',
        "data": {}
    }
    

class SavingsViewSet(custom_viewsets.ModelViewSet):
    model = Savings
    queryset = Savings.objects.all()
    serializer_class = SavingSerializers
    list_success_message = 'saving data list success'
    create_success_message = 'created the data success'
    satus_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'saving view data featch',
        "data": {}
    }


class MeetingViewSet(custom_viewsets.ModelViewSet):
    model = Meeting
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializers
    create_success_message = 'created the data'
    status_response = 200
    status_code = 200
    response = {
        "status":200,
        "msg": "successfully",
        "data":{}
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
        "msg": 'success',
        "data": {}
    }



class NotificationViewSet(custom_viewsets.ModelViewSet):
    model = Notification
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers
    list_success_message = 'Notification data of list success'
    create_success_message = 'created the Notification data'
    satus_response = 200
    status_code = 200
    response = {
        "status": 200,
        "msg": 'Notification data successfully',
        "data": {}
    }

class MicroLendingRequestViewSet(custom_viewsets.ModelViewSet):
    model = MicroLendingRequest
    queryset = MicroLendingRequest.objects.all()
    serializer_class = MicroLendingRequestSerializers
    create_success_message = 'created the data success'
    list_success_message = 'data in list'
    status_response = 200
    status_code = 200
    response = {
        "status":200,
        "msg":"success",
        "data":{}
    }