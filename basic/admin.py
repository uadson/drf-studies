from django.contrib import admin

from basic.models.course import Course
from basic.models.exam import Exam


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'url',
        'created',
        'updated',
        'active'
    ]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = [
        'course', 
        'name', 
        'email', 
        'evaluation',
        'created', 
        'updated',
        'active'
    ]
