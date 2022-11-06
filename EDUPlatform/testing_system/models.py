from django.db import models
from users.models import Student, Teacher

from EDUPlatform.mixins import DateTimeMixin

__all__ = {"Course", "Topic", "Article", "Test", "Question", "Answer", "Image", "Attempt"}


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)


class Course(models.Model, DateTimeMixin):
    course_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pk} - {self.course_name} - {self.price}"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Topic(models.Model, DateTimeMixin):
    topic_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    image = models.ManyToManyField(Image, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.topic_name}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


class Article(models.Model, DateTimeMixin):
    title = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    content = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Test(models.Model, DateTimeMixin):
    title = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=150)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"


class Question(models.Model, DateTimeMixin):
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.text}"

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model, DateTimeMixin):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} - {self.is_correct}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"


class Attempt(models.Model, DateTimeMixin):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Test id - {self.test}, student id - {self.student}, score - {self.score}"

    class Meta:
        verbose_name = "test_attempt"
        verbose_name_plural = "test_attempts"
