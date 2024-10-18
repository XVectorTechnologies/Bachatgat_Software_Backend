from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register("bachatgat",BachatGatRegistrationViewSet),
router.register("member_registration",MemberRegistrationViewSet),
router.register("bank_detail",BankDetailViewSet),
router.register("users",UserDetailViewSet),
router.register("saving_user",SavingsViewSet),
router.register("fund_distribution",FundDistributionViewSet),
router.register("meeting_",MeetingViewSet)
router.register("notification",NotificationViewSet),
router.register("micro_lending",MicroLendingRequestViewSet),
router.register("email_",UserEmailViewSet),
router.register("support_ticket",SupportTicketViewSet),
router.register("payment_",PaymentViewSet),



urlpatterns = [
    *router.urls,
    path('',include(router.urls)),
]
