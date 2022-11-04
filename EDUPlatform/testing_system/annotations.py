from dataclasses import dataclass

from django.forms import DecimalField, EmailField
from users.annotations import TeacherAnnotation

from .consts import create_course


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    course_name: str
    teacher: TeacherAnnotation
    price: DecimalField
