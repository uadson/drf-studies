from rest_framework import generics

from basic.models import Course, Exam

from basic.serializers import CourseSerializer, ExamSerializer


class CourseListCreateAPIViewInterm(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ExamListCreateAPIViewInterm(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ExamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer