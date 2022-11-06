from .annotations import (
    GroupAnnotation,
    StudentAnnotation,
    TeacherAnnotation,
    UserAnnotation,
)
from .models import Group, Student, Teacher, User

USER_DATA = {
    "password": "1234",
    "first_name": "Test_name",
    "last_name": "Test_surname",
    "email": "test_email@mail.ru",
}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(password="1234", first_name="Test_name", last_name="Test_surname", email="test_email@mail.ru")
    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=12, user=user_id)
    return teacher


def create_student(user_id) -> StudentAnnotation:
    student = Student.objects.create(age=12, rating=50, user=user_id)
    return student


def create_group(course_id, teacher_id) -> GroupAnnotation:
    group = Group.objects.create(group_name="Test_name", course=course_id, teacher=teacher_id)
    return group

