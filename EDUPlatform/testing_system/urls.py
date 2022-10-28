from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    ArticleViewSet,
    AttemptViewSet,
    CourseViewSet,
    QuestionViewSet,
    TestViewSet,
    TopicViewSet,
)

router = DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"topic", TopicViewSet)
router.register(r"article", ArticleViewSet)
router.register(r"test", TestViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"attempt", AttemptViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
