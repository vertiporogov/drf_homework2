from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course
from materials.paginators import CourseLessonPaginator
from materials.permission import IsModer, IsOwner
from materials.serializers.course import CourseSerializer
from materials.tasks import course_update


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CourseLessonPaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ['destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        return super().get_permissions()

    def perform_update(self, serializer):
        update_course = serializer.save()
        course_update.delay(update_course.id)
        update_course.save()
