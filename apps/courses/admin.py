from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from apps.courses.forms import QuestionForm

from apps.courses.models.exam import Exam
from apps.courses.models.question import Question
from apps.courses.models.question_choice import QuestionChoice

from .models.course import Course
from .models.course_category import CourseCategory
from .models.featured_course import FeaturedCourse
from .models.lesson import Lesson
from .models.material import Material

#~~~~~~~~~~~~~~~~~~~~~~~ Course ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    class LessonStackedInline(SortableStackedInline):
        model = Lesson
        extra = 0
        show_change_link = True
        fieldsets = [[None, {"fields": ['title', 'exam', 'ordering']}]]
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
        readonly_fields = ['title']
        ordering = ['ordering']

    list_display = ['ordering', 'title', 'days',
                    'totalMaterialsCount', 'course', 'exam']
    readonly_fields = ["exam"]
    inlines = [MaterialStackedInline]

#~~~~~~~~~~~~~~~~~~~~~~~ Material ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Material)
class MaterialAdmin(SortableAdminMixin, SummernoteModelAdmin):
    summernote_fields = ['content']
    list_display = ['ordering', 'id', 'title']


#~~~~~~~~~~~~~~~~~~~~~~~ Others ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'color']
    list_display_links = ['id', 'title']
    ordering = ['id']


@admin.register(FeaturedCourse)
class FeaturedCourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(SortableAdminMixin, admin.ModelAdmin):
    class QuestionStackedInline(SortableStackedInline):
        model = Question
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['title', 'ordering']}]]
        ordering = ['ordering']

    list_display = ['id', 'lesson', 'ordering', ]
    list_display_links = ['id', 'lesson']
    readonly_fields = ['lesson']
    inlines = [QuestionStackedInline]


@admin.register(Question)
class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = QuestionForm
    ordering = ['ordering']

    class ChoiceStackedInline(SortableStackedInline):
        model = QuestionChoice
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['name', 'ordering']}]]
        ordering = ['ordering']

    inlines = [ChoiceStackedInline]
