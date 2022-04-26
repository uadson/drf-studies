from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from basic.models.base import Course, Exam

from basic.serializers import CourseSerializer, ExamSerializer


class CourseAPIViewBasic(APIView):
    """
    API of Courses
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        # salva e retorna se os dados forem válidos, caso contrário retorna um exception
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ExamAPIViewBasic(APIView):
    """
    API of Exams
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
