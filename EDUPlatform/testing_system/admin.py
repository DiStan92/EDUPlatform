from django.contrib import admin

from .models import Answer, Article, Attempt, Course, Image, Question, Test, Topic


class InLineAnswer(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [InLineAnswer]


admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Image)
