from dataclasses import dataclass
from django.forms import EmailField, DecimalField


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    first_name: str
    last_name: str
    email: EmailField
    password: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    user: UserAnnotation
    experience: int


@dataclass(frozen=True, slots=True)
class StudentAnnotation:
    user: UserAnnotation
    age: int
    rating: DecimalField



