from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from basic.models.course import Course
from basic.serializers import CourseSerializer


class CoursesListCreateAPIView(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
        Show all courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
