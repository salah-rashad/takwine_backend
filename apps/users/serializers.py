from rest_framework import serializers

from ..courses.models.course import Course
from ..courses.models.lesson import Lesson
from ..courses.serializers import CourseSerializer, LessonSerializer
from ..documents.models.document import Document
from ..documents.serializers import DocumentSerializer
from .models import (Certificate, CompleteLesson, CourseBookmark,
                     DocumentBookmark, Enrollment, User)


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

    currentLesson = LessonSerializer()

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

        # converting course from "id" to actual Course "object"
        course_id = data['course']
        course = Course.objects.filter(id=course_id).first()
        if course:
            data.update({
                "course": CourseSerializer(course).data
            })

        return data


class CompleteLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompleteLesson
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'id',
            'title',
            'result',
            'date',
        ]


class CourseBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseBookmark
        fields = [
            'id',
            'user',
            'course',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # converting course from "id" to actual Course "object"
        course_id = data['course']
        course = Course.objects.filter(id=course_id).first()
        if course:
            data.update({
                "course": CourseSerializer(course).data
            })

        return data


class DocumentBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentBookmark
        fields = [
            'id',
            'user',
            'document',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # converting document from "id" to actual Document "object"
        document_id = data['document']
        document = Document.objects.filter(id=document_id).first()
        if document:
            data.update({
                "document": DocumentSerializer(document).data
            })

        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    oldPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)

