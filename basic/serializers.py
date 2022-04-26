from rest_framework import serializers

from basic.models.base import Course, Exam


class CourseSerializer(serializers.ModelSerializer):
    class Meta:

        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active'
        )


class ExamSerializer(serializers.ModelSerializer):
    class Meta:

        # email indisponível para GET, somente para POST
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Exam
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'evaluation',
            'created',
            'active',
        )
