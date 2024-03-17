from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.serializers.lesson import LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDetailAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDeleteAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
