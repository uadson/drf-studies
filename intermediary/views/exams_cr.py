from rest_framework import generics

from basic.models.exam import Exam
from basic.serializers import ExamSerializer


class ExamsListCreateAPIView(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
