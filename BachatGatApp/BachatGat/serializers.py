from rest_framework import serializers
from .models import *

class BachatGatRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BachatGatRegistration
        fields = '__all__'

class MemberRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemberRegistration
        fields = '__all__'
    
class UserDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class BankDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = '__all__'

class SavingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'


class LoanSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Loan
        fields = '__all__'

class FundDistributionSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundDistribution
        fields = '__all__'

class  MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ReportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

