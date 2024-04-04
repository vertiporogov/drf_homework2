from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test1@test1.com', is_superuser=True
        )

        self.course = Course.objects.create(
            name='Test',
            description='Test'
        )

        self.lesson = Lesson.objects.create(
            name='Test',
            course=self.course,
            owner=self.user
        )

        moderator_group, created = Group.objects.get_or_create(name='moders')

        self.user = User.objects.create(email='test@test.com', is_superuser=True)
        self.user.groups.add(moderator_group)

    def test_get_list(self):
        """ Тест для получения списка уроков """

        response = self.client.get(
            reverse('materials:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """ Тест для создания уроков """

        data = {
            "name": "test2",
            "description": "test2",
            "course": self.course,
            "owner": self.user
        }

        response = self.client.post(
            reverse('materials:create'),
            data=data
        )
        # print(response.json())

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Lesson.objects.all().exists()
        )
