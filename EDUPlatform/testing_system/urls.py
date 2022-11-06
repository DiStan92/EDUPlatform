from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    ArticleViewSet,
    AttemptViewSet,
    CourseTopicViewApi,
    CourseViewSet,
    QuestionAnswerViewApi,
    QuestionViewSet,
    TestQuestionViewApi,
    TestViewSet,
    TopicArticleViewApi,
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
    re_path("course/(?P<id>.+)/topic", CourseTopicViewApi.as_view(), name="detail_course_topic"),
    re_path("topic/(?P<id>.+)/article", TopicArticleViewApi.as_view(), name="detail_topic_article"),
    re_path("test/(?P<id>.+)/question", TestQuestionViewApi.as_view(), name="detail_test_question"),
    re_path("question/(?P<id>.+)/answer", QuestionAnswerViewApi.as_view(), name="detail_question_answer"),
]
