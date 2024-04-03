from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from materials.models import Course, Lesson, Subscription
from materials.serializers.lesson import LessonSerializer


class LessonListSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = SerializerMethodField()
    lessons = SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return [[lesson.name, lesson.description] for lesson in Lesson.objects.filter(course=course)]

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'count_lesson', 'lessons',)
