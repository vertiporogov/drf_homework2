from rest_framework import serializers

from materials.models import Lesson
from materials.validators import checking_the_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[checking_the_link])

    class Meta:
        model = Lesson
        fields = '__all__'
