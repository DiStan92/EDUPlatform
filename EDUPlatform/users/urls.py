from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import GroupStudentViewAPI, GroupViewSet, TeacherViewSet, UserViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"teacher", TeacherViewSet)
router.register(r"group", GroupViewSet)


urlpatterns = [path("", include(router.urls)), re_path("groups/(?P<id>.+)/students", GroupStudentViewAPI.as_view(), name="groups_students")]
