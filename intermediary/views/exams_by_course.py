from rest_framework import generics

from basic.models.exam import Exam
from basic.serializers import ExamSerializer


class ExamsByCourseAPIView(generics.ListCreateAPIView):
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
