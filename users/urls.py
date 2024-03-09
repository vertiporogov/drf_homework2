from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
              ] + router.urls
