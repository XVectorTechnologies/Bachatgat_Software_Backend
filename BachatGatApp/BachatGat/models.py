from django.db import models

import uuid
# Create your models here.

class MyBaseModel(models.Model):
    id = models.AutoField(primary_key= True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class BachatGatRegistration(MyBaseModel):
    bachatgat_name = models.CharField(max_length=255)
    start_month = models.CharField(max_length=50)
    start_year = models.CharField(max_length=4)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    momber_count = models.IntegerField()
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    register_by = models.UUIDField(default=uuid.uuid4, editable=False)


class MemberRegistration(MyBaseModel):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    entry_month = models.CharField(max_length=20)
    entry_year = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class BankDetail(MyBaseModel):
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class UserDetail(MyBaseModel):
    user_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    government_pro = models.CharField(max_length=255)
    bank_details_id = models.ForeignKey(BankDetail, on_delete=models.CASCADE)
    pid = models.UUIDField(default=uuid.uuid4,editable=False)



class Saving(MyBaseModel):
    member_id = models.ForeignKey(MemberRegistration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_of_contribution = models.DateField(auto_now_add=True)
    fine = models.DecimalField(max_digits=12, decimal_places=2)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class Loan(MyBaseModel):
    member_id = models.ForeignKey(MemberRegistration, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(auto_now=True)
    repayment_schedule = models.CharField(max_length=255)
    loan_status = models.CharField(max_length=50)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

class FundDistribution(MyBaseModel):
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    emergency_fund = models.DecimalField(max_digits=12, decimal_places=2)
    event_fund = models.DecimalField(max_digits=12, decimal_places=2)
    inverstment = models.DecimalField(max_digits=12, decimal_places=2)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
