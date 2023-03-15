from django.urls import path

# Courses
from intermediary.views.courses_cr import CoursesListCreateAPIView
from intermediary.views.courses_rud import CoursesRetrieveUpdateDestroyAPIView

# Exams
from intermediary.views.exams_cr import ExamsListCreateAPIView
from intermediary.views.exams_rud import ExamsRetrieveUpdateDestroyAPIView
from intermediary.views.exams_by_course import ExamsByCourseAPIView
from intermediary.views.exam_by_course import ExamByCourseAPIView


app_name = 'intermediary'

urlpatterns = [

    # Courses
    path('courses/', CoursesListCreateAPIView.as_view(), name='courses_cr'),
    path('courses/<int:pk>/', CoursesRetrieveUpdateDestroyAPIView.as_view(), name='course_rud'),

    # Exams
    path('exams/', ExamsListCreateAPIView.as_view(), name='exams_cr'),
    path('exams/<int:pk>/', ExamsRetrieveUpdateDestroyAPIView.as_view(), name='exams_rud'),

    # Exams/Exam by Course
    path('courses/<int:course_pk>/exams/', ExamsByCourseAPIView.as_view(), name='exams_by_course_id'),
    path('courses/<int:course_pk>/exams/<int:exam_pk>/', ExamByCourseAPIView.as_view(), name='exam_by_course_id'),
]
