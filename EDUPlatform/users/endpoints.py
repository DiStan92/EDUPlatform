from .models import User, Teacher, Student, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .serializers import \
    UserSerializer, TeacherSerializer, StudentSerializer, \
    GroupSerializer, GroupStudentSerializer, StudentTeacherSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class GroupStudentViewAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = GroupStudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group = self.kwargs["id"]
        print(self.request)
        return Student.objects.filter(group__in=group)

