from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from testing_system.consts import create_course

from .consts import USER_DATA, create_group, create_student, create_teacher, create_user
from .serializers import (
    GroupSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)

__all__ = {"CreateUserTest"}


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "New_name"})

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_teacher(self):
        url = reverse("teacher-list")
        response = self.client.post(url, data={"experience": 12, "user": self.user.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({"experience": 3})

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_teacher(self):
        url = reverse("student-list")
        response = self.client.post(url, data={"age": 12, "rating": 50, "user": self.user.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_student_detail(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.data = StudentSerializer(self.student).data
        self.data.update({"age": 8})

    def test_update_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_delete_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)

    def test_create_group(self):
        url = reverse("group-list")
        response = self.client.post(url, data={"group_name": "Test_name", "course": self.course.id, "teacher": self.teacher.id, "student": [self.student.id]}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


"""class ReadGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(course_id=self.course, teacher_id=self.teacher)
        self.group.student_id.set(self.student)


    def test_student_list(self):
        url = reverse("group-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_student_detail(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)"""


class UpdateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(course_id=self.course, teacher_id=self.teacher)
        self.data = GroupSerializer(self.group).data
        self.data.update({"teacher": 1})

    def test_update_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(course_id=self.course, teacher_id=self.teacher)

    def test_delete_student(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
