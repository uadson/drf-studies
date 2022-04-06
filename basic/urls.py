from django.urls import path

from basic.views import CourseAPIViewBasic, ExamAPIViewBasic


app_name = 'basic'

urlpatterns = [
    # API Courses
    path('courses/', CourseAPIViewBasic.as_view(), name='courses_basic'),

    # API Exams
    path('exams/', ExamAPIViewBasic.as_view(), name='exams_basic'),
]
