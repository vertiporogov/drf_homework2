from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView, UserListAPIView, UserCreateAPIView, UserDetailAPIView, \
    UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('', UserListAPIView.as_view(), name='user-list'),
                  path('create/', UserCreateAPIView.as_view(), name='user-create'),
                  path('detail/', UserDetailAPIView.as_view(), name='user-detail'),
                  path('update/', UserUpdateAPIView.as_view(), name='user-update'),
                  path('delete/', UserDeleteAPIView.as_view(), name='user-delete'),
              ] + router.urls
