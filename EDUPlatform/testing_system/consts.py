from .models import Course, Topic, Article, Test, Question, Answer, Image
from .annotations import CourseAnnotation, TopicAnnotation
from users.consts import create_teacher

IMAGE_MOCK = ContentFile(b"R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==", name="photo.png")


def create_image():
    image = Image.objects.create(image=IMAGE_MOCK)
    return image


def create_course(teacher_id) -> CourseAnnotation:
    course = Course.objects.create(course_name="Test_name", teacher=teacher_id, price=2000)
    return course


def create_topic(course_id) -> TopicAnnotation:
    topic = Topic.objects.create(topic_name="Test_name", course=course_id)
    return topic


def create_article(topic_id, teacher_id) -> ArticleAnnotation:
    article = Article.objects.create(title="Test_name", topic=topic_id, teacher=teacher_id)
    return article


def create_Test(topic_id, teacher_id):
    test = Test.objects.create(title='123', topic=topic_id, teacher=teacher_id, description='123', is_open=False)
    return test


def create_Question(test_id):
    question = Question.objects.create(test=test_id, text='123', is_important=False)
    return question


def create_Answer(question_id):
    answer = Answer.objects.create(question=question_id, text='123', is_correct=False)
    return answer


