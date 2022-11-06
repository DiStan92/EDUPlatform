from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.consts import USER_DATA, create_course, create_teacher, create_user
from testing_system.consts import create_Answer, create_Question, create_Test, create_topic

from .serializers import CourseSerializer


class CreateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.post(url, data={"course_name": "Math", "teacher": self.teacher.id, "price": 100}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.data = CourseSerializer(self.course).data
        self.data.update({"price": 200})

    def test_update_teacher(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_delete_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_topic(self):
        url = reverse("topic-list")
        response = self.client.post(url, data={"topic_name": "Math", "course": self.course.id, "price": 100},
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_read_topic(self):
        url = reverse("topic-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.data = TopicSerializer(self.topic).data
        self.data.update({"topic_name": "Biology"})

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_delete_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_article(self):
        url = reverse("article-list")
        response = self.client.post(url, data={"title": "Math", "topic": self.topic.id, "teacher": self.teacher.id},
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(topic_id=self.topic, teacher_id=self.teacher)

    def test_read_article(self):
        url = reverse("article-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_group_detail(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(topic_id=self.topic, teacher_id=self.teacher)
        self.data = ArticleSerializer(self.article).data
        self.data.update({"title": "Fizics"})

    def test_update_article(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(topic_id=self.topic, teacher_id=self.teacher)

    def test_delete_article(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_test(self):
        url = reverse("test-list", args=[self.test.id])
        response = self.client.post(url, data={"tittle": "123", "topic": self.topic_id,
                                    "teacher": teacher_id, "description": '123', "is_open": False}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(teacher_id=self.teacher, topic_id=self.topic)

    def test_read_test(self):
        url = reverse("test-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.data = TestSerializer(self.test).data
        self.test = create_Test(teacher_id=self.teacher, topic_id=self.topic)
        self.data.update({"tittle": "123"})

    def test_update_test(self):
        url = reverse("test-detail", args=[self.test.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(teacher_id=self.teacher, topic_id=self.topic)

    def test_delete_test(self):
        url = reverse("test-detail", args=[self.test.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.topic, self.teacher)

    def test_create_question(self):
        url = reverse("question-list", args=[self.question.id])
        response = self.client.post(url, data={"test": test_id, "text": '123', "is_important": False}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.topic, self.teacher)
        self.question = create_Question(test_id=self.test)

    def test_read_question(self):
        url = reverse("question-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.teacher, self.topic)
        self.question = create_Question(test_id=self.test)
        self.data = QuestionSerializer(self.question).data
        self.data.update({"text": "123123"})

    def test_update_question(self):
        url = reverse("question-detail", args=[self.question.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteQuestionTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.teacher, self.topic)
        self.question = create_Question(test_id=self.test)

    def test_delete_question(self):
        url = reverse("question-detail", args=[self.question.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.topic, self.teacher)
        self.question = create_Question(self.test)

    def test_create_answer(self):
        url = reverse("answer-list", args=[self.answer.id])
        response = self.client.post(url, data={"question": question_id, "text": '123', "is_correct": False},
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.topic, self.teacher)
        self.question = create_Question(self.test)
        self.answer = create_Answer(question_id=self.question)

    def test_read_answer(self):
        url = reverse("answer-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.teacher, self.topic)
        self.question = create_Question(self.test)
        self.answer = create_Answer(question_id=self.question)
        self.data = QuestionSerializer(self.question).data
        self.data.update({"text": "123123123"})

    def test_update_answer(self):
        url = reverse("answer-detail", args=[self.answer.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteAnswerTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.test = create_Test(self.teacher, self.topic)
        self.question = create_Question(self.test)
        self.answer = create_Answer(question_id=self.question)

    def test_delete_answer(self):
        url = reverse("answer-detail", args=[self.answer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

