from rest_framework import generics
from rest_framework.generics import get_object_or_404

from basic.models.exam import Exam
from basic.serializers import ExamSerializer


class ExamByCourseAPIView(generics.RetrieveUpdateDestroyAPIView):
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
