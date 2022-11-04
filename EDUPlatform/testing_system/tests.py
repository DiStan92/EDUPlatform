from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.consts import USER_DATA, create_course, create_teacher, create_user

from .serializers import CourseSerializer


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

    def test_update_teacher(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
