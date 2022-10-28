from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import CourseViewSet, TopicViewSet, ArticleViewSet


router = DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"topic", TopicViewSet)
router.register(r"article", ArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
