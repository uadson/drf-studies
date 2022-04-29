from django.db import models

from .base import Base
from .course import Course


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
