from django.core.files.base import ContentFile

from .annotations import ArticleAnnotation, CourseAnnotation, TopicAnnotation
from .models import Answer, Article, Course, Image, Question, Test, Topic

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
