from operator import indexOf

from rest_framework import serializers
from apps.courses.models.course_file import CourseFile

from apps.courses.models.exam import Exam
from apps.courses.models.lesson import Lesson
from apps.courses.models.material import Material
from apps.courses.models.material_file import MaterialFile
from apps.courses.models.question import Question
from apps.courses.models.question_choice import QuestionChoice
from takwine.serializers import TakwineFileSerializer

from .models.course import Course, CourseCategory


class CourseCategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = CourseCategory
        fields = "__all__"

    def get_icon(self, instance: CourseCategory):
        icon = instance.icon
        return str(icon).split("icon:")[1]


class CourseFileSerializer(TakwineFileSerializer):
    class Meta:
        model = CourseFile
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer()
    guideFile = CourseFileSerializer()
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
            "guideFile",
            "videoUrl",
            "date",
            "enabled",
            "days",
            "totalEnrollments",
        ]


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

        for item in lessons:
            if item == instance:
                return indexOf(lessons, item) + 1


class MaterialFileSerializer(TakwineFileSerializer):
    class Meta:
        model = MaterialFile
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    ordering = serializers.SerializerMethodField()
    files = MaterialFileSerializer(many=True)

    class Meta:
        model = Material
        fields = [
            'id',
            'lesson',
            'title',
            'content',
            'ordering',
            'files',
        ]

    def get_ordering(self, instance: Material):
        materials: list[Material] = instance.lesson.materials()

        for item in materials:
            if item == instance:
                return indexOf(materials, item)+1


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
