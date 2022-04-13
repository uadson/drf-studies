from django.urls import path

from intermediary.views import ListCreateAPIViewCoursesInterm, ExamListCreateAPIViewInterm
from intermediary.views import RetrieveUpdateDestroyAPIViewCoursesInterm
from intermediary.views import ExamsByCourseAPIViewInterm
from intermediary.views import ExamByCourseAPIViewInterm


app_name = 'intermediary'

urlpatterns = [
    path('courses/', ListCreateAPIViewCoursesInterm.as_view(), name='courses'),
    path('courses/<int:pk>/', RetrieveUpdateDestroyAPIViewCoursesInterm.as_view(), name='course'),
    path('courses/<int:course_pk>/exams', ExamsByCourseAPIViewInterm.as_view(), name='exams_by_course_id'),
    path('courses/<int:course_pk>/exams/<int:exam_pk>/', ExamByCourseAPIViewInterm.as_view(), name='exam_by_course_id'),

    path('exams/', ExamListCreateAPIViewInterm.as_view(), name='exams'),
    path('exams/<int:exam_pk>/', ExamByCourseAPIViewInterm.as_view(), name='exam'),
]
