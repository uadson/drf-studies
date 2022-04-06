from django.urls import path

from intermediary.views import CourseListCreateAPIViewInterm, ExamListCreateAPIViewInterm
from intermediary.views import CourseRetrieveUpdateDestroyAPIView, ExamRetrieveUpdateDestroyAPIView


app_name = 'intermediary'

urlpatterns = [
    path('courses/', CourseListCreateAPIViewInterm.as_view(), name='courses'),

    path('exams/', ExamListCreateAPIViewInterm.as_view(), name='exams'),

    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course'),

    path('exams/<int:pk>/', ExamRetrieveUpdateDestroyAPIView.as_view(), name='exam'),
]
