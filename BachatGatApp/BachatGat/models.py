from django.db import models
import uuid

# Base Model with AutoField and timestamp fields
class MyBaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# BachatGatRegistration Model
class BachatGatRegistration(MyBaseModel):
    bachatgat_name = models.CharField(max_length=255)
    start_month = models.CharField(max_length=50)
    start_year = models.CharField(max_length=4)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    member_count = models.IntegerField()
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    register_by = models.UUIDField(default=uuid.uuid4, editable=False)

# MemberRegistration Model
class MemberRegistration(MyBaseModel):
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    member_pid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    entry_month = models.CharField(max_length=20)
    entry_year = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

# UserDetail Model
class UserDetail(MyBaseModel):
    user_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    government_proof = models.CharField(max_length=255)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

# BankDetail Model
class BankDetail(MyBaseModel):
    user_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

# Savings Model
class Savings(MyBaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_of_contribution = models.DateField(auto_now_add=True)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

# FundDistribution Model
class FundDistribution(MyBaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
    ]
    
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    saving_id = models.ForeignKey(Savings, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    loan_status = models.CharField(max_length=50)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

# Meeting Model
class Meeting(MyBaseModel):
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    meeting_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    agenda = models.TextField(blank=True, null=True)

# Notification Model
class Notification(MyBaseModel):
    user_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    message_text = models.TextField(blank=True, null=True)
    notification_type = models.CharField(max_length=50)
    date_sent = models.DateField(auto_now_add=True)

class MicroLendingRequest(MyBaseModel):
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    member_id = models.ForeignKey(MemberRegistration, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)
    repayment_term = models.IntegerField()
    repayment_start_date = models.DateField(auto_now_add=True)
    repayment_end_date = models.DateField(auto_now_add=True)