from rest_framework import serializers

from apps.courses.models.lesson import Lesson
from apps.users.models import Enrollment

from .models.course import Course, CourseCategory


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=CourseCategory.objects.all())

    # days = serializers.SerializerMethodField("calculateDays")
    # totalEnrollments = serializers.SerializerMethodField(
    #     "calculateTotalEnrollments")

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "category",
            "imageUrl",
            "pdfUrl",
            "videoUrl",
            "date",
            "enabled",
            "days",
            "totalEnrollments",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        category_id = data['category']
        category = CourseCategory.objects.filter(id=category_id).first()
        if category:
            data.update({
                "category": CourseCategorySerializer(category).data
            })
        return data

    


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'description',
            'ordering',
            'days',
        ]
