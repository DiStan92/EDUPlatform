from rest_framework import serializers

from .models import Group, Student, Teacher, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, object):
        match isinstance(object, Student):
            case True:
                serializer = StudentSerializer(object)
            case False:
                serializer = GroupSerializer(object)
            case _:
                raise Exception('nothing to serialize. Chooses are Group, Student')
        return serializer.data
