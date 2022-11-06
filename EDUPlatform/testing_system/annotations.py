from dataclasses import dataclass

from django.forms import DecimalField, EmailField, ImageField
from users.annotations import TeacherAnnotation


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    course_name: str
    teacher: TeacherAnnotation
    price: DecimalField


@dataclass(frozen=True, slots=True)
class TopicAnnotation:
    topic_name: str
    course: CourseAnnotation
    image: ImageField
