from django.db import models

<<<<<<< HEAD
from basic.models.base import Base
=======
from models.base import Base
>>>>>>> 153a4248d6b148814860a78d23fe0f2cb8e0befd


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
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> 153a4248d6b148814860a78d23fe0f2cb8e0befd
