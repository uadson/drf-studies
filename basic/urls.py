from django.urls import path

from basic.views import CourseAPIView, ExamAPIView


app_name = 'basic'

urlpatterns = [
    # API Courses
    path('courses/', CourseAPIView.as_view(), name='courses'),

    # API Exams
    path('exams/', ExamAPIView.as_view(), name='exams'),
]
