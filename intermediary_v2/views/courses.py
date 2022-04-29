from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from basic.models.course import Course
from basic.serializers import CourseSerializer


"""
    API V2
"""


class CourseViewSet(viewsets.ModelViewSet):
    """GET, PUT, UPDATE and DELETE
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
