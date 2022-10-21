from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from EDUPlatform.mixins import DateTimeMixin
from .managers import CustomUserManager


__all__ = {"User", "Teacher", "Student", "Group"}


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):

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


class Teacher(models.Model, DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.IntegerField(verbose_name="Teacher's XP")

    def __str__(self):
        return f"{self.pk} - {self.user}"

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"


class Student(models.Model, DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.pk} - {self.user}"

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"


class Group(models.Model, DateTimeMixin):
    group_name = models.CharField(max_length=50)
    course = models.ForeignKey("testing_system.Course", on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.group_name}"

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"
