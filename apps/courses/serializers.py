from multiprocessing.managers import BaseManager
from operator import indexOf
from rest_framework import serializers
from apps.courses.models.exam import Exam

from apps.courses.models.lesson import Lesson
from apps.courses.models.material import Material
from apps.courses.models.question import Question
from apps.courses.models.question_choice import QuestionChoice
from apps.users.models import Enrollment

from .models.course import Course, CourseCategory


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
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
    ordering = serializers.SerializerMethodField("getActualOrder")

    class Meta:
        model = Lesson
        fields = [
            'id',
            'course',
            'title',
            'description',
            'days',
            'totalMaterialsCount',
            'ordering',
        ]

    def getActualOrder(self, instance: Lesson):
        lessons: list[Lesson] = instance.course.lessons()

        for l in lessons:
            if l.id == instance.id:
                return indexOf(lessons, l)+1


class MaterialSerializer(serializers.ModelSerializer):
    ordering = serializers.SerializerMethodField("getActualOrder")

    class Meta:
        model = Material
        fields = [
            'id',
            'lesson',
            'title',
            'content',
            'ordering',
        ]

    def getActualOrder(self, instance: Material):
        materials: list[Material] = instance.lesson.materials()

        for m in materials:
            if m.id == instance.id:
                return indexOf(materials, m)+1


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'choices',
            'answer',
            'ordering',
        ]

    def to_representation(self, instance: Question):
        data = super().to_representation(instance)

        choices = data.get('choices')
        if choices:
            choicesList = list(map(lambda x: x.name, choices))
            data.update({
                "choices": choicesList
            })

        answer = data.get('answer')
        if answer:
            ans = QuestionChoice.objects.filter(id=answer).first()
            if ans:
                data.update({
                    "answer": ans.name
                })
        return data


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            'id',
            'lesson',
            'questions',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        questions = data.get('questions')
        serializer = QuestionSerializer(questions, many=True)
        if questions:
            data.update({
                "questions": serializer.data
            })
        return data
