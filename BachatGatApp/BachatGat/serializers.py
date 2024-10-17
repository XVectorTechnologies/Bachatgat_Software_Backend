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

class SavingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'



class FundDistributionSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundDistribution
        fields = '__all__'

class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class MicroLendingRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = MicroLendingRequest
        fields = '__all__'
