from django.urls import path

from rest_framework.routers import SimpleRouter

from .views.courses import CourseViewSet

from .views.exams import ExamViewSet


app_name = 'intermediary_v2'

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('exams', ExamViewSet)


urlpatterns = [
    # Courses

    # Exams
]
