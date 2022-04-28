from rest_framework import generics

from basic.models.course import Course
from basic.serializers import CourseSerializer


class CoursesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
