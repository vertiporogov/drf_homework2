from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls
