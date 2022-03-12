from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=100)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.title


class Exam(Base):
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
