from rest_framework import viewsets

from basic.models.exam import Exam
from basic.serializers import ExamSerializer


"""
API V2
"""


class ExamViewSet(viewsets.ModelViewSet):
    """GET, PUT, UPDATE, DELETE
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
