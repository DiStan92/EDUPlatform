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
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f'{self.pk} - {self.email}'
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(User):
    experiense = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ['first_name', 'last_name']


class Student(User):
    age = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['first_name', 'last_name']
