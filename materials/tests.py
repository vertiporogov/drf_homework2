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

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materials:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """ Тест создания уроков """

        self.client.force_authenticate(user=self.user)

        data = {
            "name": self.lesson.name,
            "course": self.course.id,
            "owner": self.user.id,
            "link" : "https://youtube.com"
        }

        response = self.client.post(
            '/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Lesson.objects.all().exists()
        )
        # self.assertEqual(
        #     response.json()['name'],
        #     data['name']
        # )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""
        self.client.force_authenticate(user=self.user)
        lesson = Lesson.objects.create(
            name='Test_lesson',
            description='Test_lesson',
            owner=self.user,
            link="https://youtube.com"
        )

        response = self.client.patch(
            f'/{lesson.id}/update/',
            {'description': 'change'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        self.client.force_authenticate(user=self.user)

        lesson = Lesson.objects.create(
            name='Test_lesson',
            description='Test_lesson',
            owner=self.user,
            link="https://youtube.com"
        )

        response = self.client.delete(
            f'/{lesson.id}/delete/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test3@test3.com', is_superuser=True
        )

        self.course = Course.objects.create(
            name='Test3',
            description='Test3'
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

        moderator_group, created = Group.objects.get_or_create(name='moders')

        self.user = User.objects.create(email='test@test.com', is_superuser=True)
        self.user.groups.add(moderator_group)

    def test_subscribe_to_course(self):
        """Тест на создание подписки на курс"""
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "course_id": self.course.id,
        }

        response = self.client.post(
            reverse('materials:subscription'),
            data=data
        )
        # print(response.json())
        #
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'Подписка на курс добавлена'}
        )
