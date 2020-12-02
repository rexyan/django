from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# Question，Choice 注册到 admin 中
admin.site.register(Question)
admin.site.register(Choice)
