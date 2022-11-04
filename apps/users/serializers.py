from rest_framework import serializers

from apps.courses.models.material import Material
from apps.courses.serializers import CourseSerializer, LessonSerializer
from apps.users.intermediates import CompleteLesson

from ..courses.models.course import Course
from ..courses.models.lesson import Lesson
from .models import Enrollment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'password',
            'birthDate',
            'email',
            'imageUrl',
            'phoneNumber',
            'city',
            'job',
            'is_staff'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class EnrollmentSerializer(serializers.ModelSerializer):

    # completeLessons = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     allow_null=True,
    # )

    # progress = serializers.SerializerMethodField("getProgress")
    # isComplete = serializers.SerializerMethodField("getIsComplete")

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'created_at',
            'user',
            'course',
            'currentLesson',
            'progress',
            'isComplete',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # extra = {}

        # converting "course" from id to actual Course object
        course_id = data['course']
        course = Course.objects.filter(id=course_id).first()

        # converting "currentLesson" from id to actual Lesson object
        currentLesson_id = data['currentLesson']
        currentLesson = Lesson.objects.filter(id=currentLesson_id).first()

        if course:
            data.update({
                "course": CourseSerializer(course).data
            })
        if currentLesson:
            data.update({
                "currentLesson": LessonSerializer(currentLesson).data
            })

        # data.update(extra)
        return data


class CompleteLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompleteLesson
        fields = '__all__'
