from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register("bachatgat", BachatGatRegistrationViewSet),
routers.register("member_registration",MemberRegistrationViewSet),
routers.register("bank_detail",BankDetailViewSet),
routers.register("users",UserDetailViewSet),
routers.register("saving_user",SavingsViewSet),
routers.register("loan_",LoanViewSet),
routers.register("fund_distribution",FundDistributionViewSet),

routers.register("meeting_", MeetingViewSet),
routers.register("employee_attendance",AttendanceViewSet),
routers.register("reports_",ReportsViewSet),

urlpatterns = [
    *routers.urls,
    path('',include(routers.urls)),
]