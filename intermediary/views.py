from rest_framework.generics import get_object_or_404
from rest_framework import generics

from basic.models.base import Course, Exam

from basic.serializers import CourseSerializer, ExamSerializer


class ListCreateAPIViewCoursesInterm(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
        Show all courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetrieveUpdateDestroyAPIViewCoursesInterm(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ExamsByCourseAPIViewInterm(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods 
    """
    # show all exams by course_id
    
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        # return a list of objects

        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class ExamByCourseAPIViewInterm(generics.RetrieveUpdateDestroyAPIView):
    """
        Show one exam by id or one exam by course_id
        Retrieve, Update and Destroy -> GET, PUT, DELETE methods
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_object(self):
        # return one object

        if self.kwargs.get('course_pk'):
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('exam_pk')
            )

        return get_object_or_404(
            self.get_queryset(), 
            pk=self.kwargs.get('exam_pk')
        )


class ExamListCreateAPIViewInterm(generics.ListCreateAPIView):
    """
        List and Create -> GET, POST methods
        Show all exams
    """
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
