from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.pk} - {self.email}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.user}"

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pk} - {self.user}"

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.course_name}, {self.teacher}, {self.price}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()

    def __str__(self):
        return f"{self.topic_name}, {self.course}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


class Article(models.Model):
    title = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Test(models.Model):
    title = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=150)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.teacher}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.topic}, {self.text}"

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}, {self.is_correct}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
