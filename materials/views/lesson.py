from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.paginators import CourseLessonPaginator
from materials.permission import IsModer, IsOwner
from materials.serializers.lesson import LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]
    pagination_class = CourseLessonPaginator


class LessonDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDeleteAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    # def get_queryset(self):
    #     queryset = Lesson.objects.all()
    #     return queryset


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]
