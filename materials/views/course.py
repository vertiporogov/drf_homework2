from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course
from materials.permission import IsModer, IsOwner
from materials.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    # Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами,
    # но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры

    # Опишите права доступа для объектов таким образом, чтобы пользователи,
    # которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ['destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        return super().get_permissions()
