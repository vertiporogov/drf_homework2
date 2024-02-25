from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet
from materials.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDetailAPIView, \
    LessonDeleteAPIView

app_name = MaterialsConfig.name


router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns = [
    path('', LessonListAPIView.as_view()),
    path('create/', LessonCreateAPIView.as_view()),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view()),
    path('<int:pk>/', LessonDetailAPIView.as_view()),
    path('<int:pk>/delete/', LessonDeleteAPIView.as_view()),
] + router.urls
