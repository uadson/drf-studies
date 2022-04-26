from django.db import models

from models.base import Base


class Course(Base):
    """Class Course

    Args:
        Base: Class Abstract

    Returns:
        str: title
    """
    title = models.CharField(max_length=100)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        
    def __str__(self):
        return self.title