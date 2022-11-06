from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.consts import USER_DATA, create_teacher, create_user

from .consts import create_course, create_topic
from .serializers import CourseSerializer, TopicSerializer

"""def test_create_image(self):
        url = reverse("image-list")
        response = self.client.post(url, data={"image": self.image.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)"""


class CreateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.post(url, data={"course_name": "Math", "teacher": self.teacher.id, "price": 100}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.data = CourseSerializer(self.course).data
        self.data.update({"price": 200})

    def test_update_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_delete_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_topic(self):
        url = reverse("topic-list")
        response = self.client.post(url, data={"topic_name": "Math", "course": self.course.id, "price": 100}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_read_topic(self):
        url = reverse("topic-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.data = TopicSerializer(self.topic).data
        self.data.update({"topic_name": "Biology"})

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_delete_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
