from rest_framework import serializers

word = 'youtube.com'


def checking_the_link(value):
    if not value.endswith(word):
        raise serializers.ValidationError('Это запрещенная ссылка')
