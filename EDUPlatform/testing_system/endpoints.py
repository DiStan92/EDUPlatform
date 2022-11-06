from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Answer, Article, Attempt, Course, Question, Test, Topic
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    AttemptSerializer,
    CourseSerializer,
    QuestionSerializer,
    TestSerializer,
    TopicSerializer,
)

CUSTOM = [permissions.AllowAny]
ADMINS = [permissions.IsAdminUser]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = CUSTOM


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = CUSTOM


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = CUSTOM


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = CUSTOM


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = CUSTOM


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = CUSTOM


class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = CUSTOM


class CourseTopicViewApi(ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = CUSTOM

    def get_queryset(self):
        course = self.kwargs["id"]
        return Topic.objects.filter(course_id=course)


class TopicArticleViewApi(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = CUSTOM

    def get_queryset(self):
        topic = self.kwargs["id"]
        return Article.objects.filter(topic_id=topic)


class TestQuestionViewApi(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = CUSTOM

    def get_queryset(self):
        test = self.kwargs["id"]
        return Question.objects.filter(test_id=test)


class QuestionAnswerViewApi(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = CUSTOM

    def get_queryset(self):
        question = self.kwargs["id"]
        return Answer.objects.filter(question_id=question)
