from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from django.contrib import admin, messages
from django_summernote.admin import SummernoteModelAdmin

from .forms import QuestionForm
from .models.course import Course
from .models.course_category import CourseCategory
from .models.course_file import CourseFile
from .models.exam import Exam
from .models.featured_course import FeaturedCourse
from .models.lesson import Lesson
from .models.material import Material
from .models.material_file import MaterialFile
from .models.question import Question
from .models.question_choice import QuestionChoice

#~~~~~~~~~~~~~~~~~~~~~~~ Course ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    class LessonStackedInline(SortableStackedInline):
        model = Lesson
        extra = 0
        show_change_link = True
        fieldsets = [[None, {"fields": ['title', 'ordering']}]]
        readonly_fields = ["exam"]
        ordering = ['ordering']

    list_display = ['id', 'title', 'category', 'lessons_count', 'days',
                    'enabled', 'totalEnrollments',  'ordering', ]
    list_filter = ['enabled', 'category__title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['id', 'title', 'category', 'enabled', ]
    inlines = [LessonStackedInline]


#~~~~~~~~~~~~~~~~~~~~~~~ Lesson ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Lesson)
class LessonAdmin(SortableAdminMixin, admin.ModelAdmin):
    class MaterialStackedInline(SortableStackedInline):
        model = Material
        extra = 0
        show_change_link = True
        fieldsets = [[None, {"fields": ['title', 'ordering']}]]
        ordering = ['ordering']

    class QuestionStackedInline(SortableStackedInline):
        model = Question
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['title', 'ordering']}]]
        ordering = ['ordering']

    list_display = ['ordering', 'title', 'days',
                    'totalMaterialsCount', 'course', 'exam']
    readonly_fields = ['exam']
    inlines = [MaterialStackedInline, QuestionStackedInline]

#~~~~~~~~~~~~~~~~~~~~~~~ Material ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Material)
class MaterialAdmin(SortableAdminMixin, SummernoteModelAdmin):
    class FileStackedInline(SortableStackedInline):
        model = MaterialFile
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['name', 'file', 'ordering']}]]
        ordering = ['ordering']

    summernote_fields = ['content']
    list_display = ['ordering', 'id', 'title']
    readonly_fields = ['lesson']
    inlines = [FileStackedInline]


#~~~~~~~~~~~~~~~~~~~~~~~ Others ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'color']
    list_display_links = ['id', 'title']
    ordering = ['id']


@admin.register(CourseFile)
class CourseFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file']
    list_display_links = ['id', 'name', 'file']
    fieldsets = [
        [None, {"fields": ['name', 'file']}]]


@admin.register(FeaturedCourse)
class FeaturedCourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


# @admin.register(Exam)
# class ExamAdmin(SortableAdminMixin, admin.ModelAdmin):
#     class QuestionStackedInline(SortableStackedInline):
#         model = Question
#         extra = 0
#         show_change_link = True
#         fieldsets = [
#             [None, {"fields": ['title', 'ordering']}]]
#         ordering = ['ordering']

#     list_display = ['id', 'lesson', 'course', 'ordering', ]
#     list_display_links = ['id', 'lesson']
#     readonly_fields = ['lesson']
#     inlines = [QuestionStackedInline]


@admin.register(Question)
class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    class ChoiceStackedInline(SortableStackedInline):
        model = QuestionChoice
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['name', 'ordering']}]]
        ordering = ['ordering']

    form = QuestionForm
    ordering = ['ordering']
    # fieldsets = [
    #     [None, {"fields": ['exam', 'title', 'answer']}]
    # ]
    readonly_fields = ['lesson']
    inlines = [ChoiceStackedInline]
    list_display = ["title", "lesson", "ordering"]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        if obj:
            answer = obj.answer
            if answer is None:
                messages.add_message(request, messages.WARNING,
                                     'Answer is not assigned')
        return fields


@admin.register(MaterialFile)
class MaterialFileAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
