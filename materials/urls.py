from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet
from materials.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDetailAPIView, \
    LessonDeleteAPIView
from materials.views.payment import PaymentListAPIView, PaymentCreateAPIView
from materials.views.subscription import SubscriptionView

app_name = MaterialsConfig.name

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns = [
                  path('', LessonListAPIView.as_view(), name='list'),
                  path('create/', LessonCreateAPIView.as_view(), name='create'),
                  path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='update'),
                  path('<int:pk>/', LessonDetailAPIView.as_view(), name='detail'),
                  path('<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='delete'),

                  path('subscription/', SubscriptionView.as_view(), name='subscription'),

                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
              ] + router.urls
