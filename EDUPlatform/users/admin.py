from django.contrib import admin

from .models import Article, Course, Student, Teacher, Topic, User

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Article)
