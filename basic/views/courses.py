from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from basic.models.course import Course

from basic.serializers import CourseSerializer


class CourseAPIViewBasic(APIView):
    """
    API of Courses

    # Get and Post from Model Course
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
