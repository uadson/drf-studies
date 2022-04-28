from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from basic.models.exam import Exam
from basic.serializers import ExamSerializer


class ExamsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
