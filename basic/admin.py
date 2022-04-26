from django.contrib import admin

from basic.models.base import Course, Exam


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
