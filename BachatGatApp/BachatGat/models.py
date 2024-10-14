from django.db import models
import uuid

# Create your models here.
class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

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


class MemberRegistration(MyBaseModel):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    entry_month = models.CharField(max_length=20)
    entry_year = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)


class BankDetail(MyBaseModel):
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class UserDetail(MyBaseModel):
    user_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    government_pro = models.CharField(max_length=255)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    bank_details_id = models.ForeignKey(BankDetail, on_delete=models.CASCADE)


class Savings(MyBaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
    ]
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,  default='USD' )
    member_id = models.ForeignKey(MemberRegistration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_of_contribution = models.DateField(auto_now_add=True)
    fine = models.DecimalField(max_digits=12, decimal_places=2)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class Loan(MyBaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
    ]
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,  default='USD' )
    member_id = models.ForeignKey(MemberRegistration,on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=12,decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(auto_now=True)
    repayment_schedule = models.CharField(max_length=255)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    loan_status = models.CharField(max_length=50)


class FundDistribution(MyBaseModel):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR', 'Indian Rupee'),
    ]
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,  default='USD' )
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    emergency_fund = models.DecimalField(max_digits=12, decimal_places=2)
    event_fund = models.DecimalField(max_digits=12, decimal_places=2)
    inverstment = models.DecimalField(max_digits=12, decimal_places=2)
    pid = models.UUIDField(default=uuid.uuid4, editable=False)


class Meeting(MyBaseModel):
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    meeting_date = models.DateField(auto_now_add=True)
    agenda = models.TextField()
    minutes = models.TextField()
    pid = models.UUIDField(default=uuid.uuid4, editable=False)

class Attendance(MyBaseModel):
    pid = models.UUIDField(default=uuid.uuid4,editable=False)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    member_id = models.ForeignKey(MemberRegistration, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=50)

class Reports(MyBaseModel):
    pid = models.UUIDField(default=uuid.uuid4, editable=False)
    bachatgat_id = models.ForeignKey(BachatGatRegistration, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)
    report_file = models.CharField(max_length=255)
    generated_date = models.DateField(auto_now_add=True)
