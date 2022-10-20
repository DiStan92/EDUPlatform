from rest_framework import serializers

from .models import Student, Teacher, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, object):
        match isinstance(object, Student):
            case True:
                serializer = StudentSerializer(object)
            case False:
                serializer = TeacherSerializer(object)
            case _:
                raise Exception('nothing true serializer')
        return serializer.data
