from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from basic.models.exam import Exam

from basic.serializers import ExamSerializer


class ExamAPIViewBasic(APIView):
    """
    API of Exams

    # Get and Post from Model Exam
    """
    def get(self, request):
        exams = Exam.objects.all()
        serialized = ExamSerializer(exams, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
