from django.shortcuts import render

# Create your views here

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
        "status": None,
        "msg":None,
        "data": None
    }
    
    @api_view(['POST'])
    def bachatgat_registration(request):
        self.response.update({
            "status": 200,
            "msg": 'bachatgat data view featch',
            "data": {}
        })
        return Response(self.response)

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
        "status":None,
        "msg": None,
        "data": None
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
        "status": None,
        "msg":None,
        "data":None 
    }

    @api_view(['POST'])
    def member_registration(request):
        self.response.update({
            "status": 200,
            "msg": "member ",
            "data": {}
        })
        return response(self.response)


class BankDetailsViewSet(custom_viewsets.ModelViewSet):
    model = BankDetails
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailSerializers
    list_success_message = "bank detail in the list success"
    retrieve_sucess_message ="retrieve returend success"
    create_success_message = "bank details created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @api_view(['POST'])
    def bank_detail(request):
        self.response.update ({
            "status": 200,
            "msg": 'bank detail the data featch',
            "data": {}
        })
        return Response(self.response)


class SavingsViewSet(custom_viewsets.ModelViewSet):
    model = Savings
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializers
    list_success_message = 'saving data list success'
    create_success_message = 'created the data success'
    satus_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @api_view(['POST'])
    def saving_(request):
        self.response.update ({
            "status":200,
            "msg": 'data view featch',
            "data":{}
        })
        return Response(self.response)

class LoanViewSet(custom_viewsets.ModelViewSet):
    model = Loan
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers
    list_success_message = 'data in list success'
    create_success_message = 'creted the data success'
    satus_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @api_view(['POST'])
    def saving_(request):
        self.response.update ({
            "status":200,
            "msg": 'data view featch successfully',
            "data":{}
        })
        return Response(self.response)

class FundDistributionViewSet(custom_viewsets.ModelViewSet):
    model = FundDistribution
    queryset = FundDistribution.objects.all()
    serializer_class = FundDistributionSerializers
    list_success_message = 'data of list success'
    create_success_message = 'created the data'
    satus_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

