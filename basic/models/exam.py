from django.db import models

<<<<<<< HEAD:basic/models/exam.py
from basic.models.base import Base

from basic.models.course import Course

=======
from models.base import Base
from models.course import Course

>>>>>>> 153a4248d6b148814860a78d23fe0f2cb8e0befd:basic/models.py

class Exam(Base):
    """Class Exam

    Args:
        Base: abstract

    Returns:
        str: name, course and evaluation
    """
    course = models.ForeignKey(Course, related_name='exams', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    evaluation = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} rated the {self.course} with {self.evaluation}'
