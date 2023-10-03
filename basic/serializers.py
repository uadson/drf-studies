from rest_framework import serializers

from basic.models.course import Course
from basic.models.exam import Exam


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


class CourseSerializer(serializers.ModelSerializer):
    class Meta:

        #### Nested Relationship
        # Return a exams list relationship with cours read only
        # Recommended relationship OneToOne Relation
        # exams = ExamSerializer(many=True, read_only=True)
        
        #### Hyper Linked Related Field
        exams = serializers.HyperlinkedRelatedField(
            many=True, 
            read_only=True, 
            view_name='exam-detail'
        )
        
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'created',
            'active',
            'exams',
        ]