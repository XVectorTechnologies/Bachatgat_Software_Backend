from django.shortcuts import render




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
        "status":None,
        "msg":None,
        "data": None
    }

    @api_view(['POST'])
    def bachatgat_registration(request):
        self.response.update ({
            "status":200,
            "msg": 'bachatgat registration data view featch',
            "data":{}
        })
        return Response(self.response)
    

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
    def member_register(request):
        self.response.update({
            "status":200,
            "msg": 'member register view data featch ',
            "data":{}
        })
        return Response(self.response)

class UserDetailViewSet(custom_viewsets.ModelViewSet):
    model = UserDetail
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializers
    list_success_message = "list the data success"
    create_success_message = "user detail created the data success"
    status_response = 200
    status_code = 200
    response = {
        "status":None,
        "msg": None,
        "data":None
    }

    @api_view(['POST'])
    def user_detail(request):
        self.response.update({
            "status": 200,
            "msg": 'user detail data view featch',
            "data":{}
        })
        return Response(self.response)


class BankDetailViewSet(custom_viewsets.ModelViewSet):
    model = BankDetail
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializers
    list_success_message = 'bank deatil of data list success '
    create_success_message = 'created the bank deatil data'
    status_response = 200
    status_code = 200
    response = {
        "status": None,
        "msg":None,
        "data":{}
    }

    @api_view(['POST'])
    def bank_deatil(request):
        self.response.update({
            "status":200,
            "msg":'iew data featch successfully',
            "data":{}
        })
        return Response(self.response)


class SavingViewSet(custom_viewsets.ModelViewSet):
    model = Saving
    queryset = Saving.objects.all()
    serializer_class = SavingSerializers
    list_success_message = 'saving the data in list success'
    create_success_message = 'created saving data success'
    status_response = 200
    status_code = 200
    response = {
        "status":None,
        "msg":None,
        "data":None
    }

    @api_view(['POST'])
    def saving_account(request):
        self.response.update({
            "status":200,
            "msg": 'saving deatil successfull',
            "data":{}
        })
        return Response(self.response)

class LoanViewSet(custom_viewsets.ModelViewSet):
    model = Loan
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers
    list_success_message = 'loan data list success'
    create_success_message = 'created loan data success'
    status_response = 200
    status_code = 200
    response = {
        "status":None,
        "msg":None,
        "data":None
    }

    @api_view(['POST'])
    def loan_(request):
        self.response.update ({
            "status": 200,
            "msg":'view data featch success',
            "data":{}
        })
        return Response(self.response)

class FundDistributionViewSet(custom_viewsets.ModelViewSet):
    model = FundDistribution
    queryset = FundDistribution.objects.all()
    serializer_class = FundDistributionSerializers
    list_success_message = 'list the data success'
    create_success_message = 'created the data in success'
    status_response = 200
    status_code = 200
    response = {
        "status":None,
        "msg":None,
        "data":None
    }

    @api_view(['POST'])
    def fund_distribution(request):
        self.response.update({
            "status":200,
            "msg":'successfully',
            "data":{}
        })
        return Response(self.response)
