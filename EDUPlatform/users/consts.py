from .models import User, Teacher, Student, Group
from .annotations import UserAnnotation, TeacherAnnotation, StudentAnnotation
from testing_system.models import Course


USER_DATA = {
    "password": "1234",
    "first_name": "Test_name",
    "last_name": "Test_surname",
    "email": "test_email@mail.ru",
}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(
        password="1234", first_name="Test_name",
        last_name="Test_surname", email="test_email@mail.ru")
    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=12, user=user_id)
    return teacher


def create_student(user_id) -> StudentAnnotation:
    student = Student.objects.create(age=12, rating=50, user=user_id)
    return student


def create_course(teacher_id):
    course = Course.objects.create(course_name="Test_name", teacher=teacher_id, price=2000)
    return course


def create_group(course_id, teacher_id):
    group = Group.objects.create(group_name="Test_name", course=course_id, teacher=teacher_id)
    return group
