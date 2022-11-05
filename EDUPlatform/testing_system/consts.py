from .models import Answer, Article, Course, Question, Test, Topic


def create_course(teacher_id):
    course = Course.objects.create(course_name="Test_name", teacher=teacher_id, price=2000)
    return course
