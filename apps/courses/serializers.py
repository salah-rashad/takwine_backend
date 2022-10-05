from unicodedata import category
from rest_framework import serializers

from .models import Course, CourseCategory


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=CourseCategory.objects.all())

    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        category_id = ret.pop('category', None)
        category = CourseCategory.objects.filter(id=category_id).first()
        if category:
            extra_ret = {
                "category": CourseCategorySerializer(category).data
            }
        ret.update(extra_ret)
        return ret
