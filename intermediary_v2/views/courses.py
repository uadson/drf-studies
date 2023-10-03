from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from basic.models.course import Course
from basic.serializers import CourseSerializer
from basic.serializers import ExamSerializer


"""
    API V2
"""


class CourseViewSet(viewsets.ModelViewSet):
    """GET, PUT, UPDATE and DELETE
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
    @action(detail=True, methods=['GET'])
    def exams(self, request, pk=None):
        """
            Obtem as avaliações do curso
        """
        course = self.get_object()
        serializer = ExamSerializer(course.exams.all(), many=True)
        return Response(serializer.data)
