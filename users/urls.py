from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserViewSet, UserListAPIView, UserCreateAPIView, UserDetailAPIView, \
    UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  path('', UserListAPIView.as_view(), name='user-list'),
                  path('create/', UserCreateAPIView.as_view(), name='user-create'),
                  path('detail/', UserDetailAPIView.as_view(), name='user-detail'),
                  path('update/', UserUpdateAPIView.as_view(), name='user-update'),
                  path('delete/', UserDeleteAPIView.as_view(), name='user-delete'),
              ] + router.urls
