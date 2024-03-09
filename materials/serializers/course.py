from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson
from materials.serializers.lesson import LessonSerializer


class LessonListSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return [[lesson.name, lesson.description] for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ('name', 'description', 'count_lesson', 'lessons',)
