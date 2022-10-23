from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from django.contrib import admin

from .models.course import Course
from .models.course_category import CourseCategory
from .models.featured_course import FeaturedCourse
from .models.lesson import Lesson
from .models.material import Material
from .models.material_attachment import MaterialAttachment
from .models.material_component import MaterialComponent

#~~~~~~~~~~~~~~~~~~~~~~~ Course -> Lessons ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):

    class LessonStackedInline(SortableStackedInline):
        model = Course.lessons.through
        extra = 0

    list_display = ['id', 'title', 'category', 'lessons_count', 'days',
                    'enabled', 'totalEnrollments',  'ordering', ]
    list_filter = ['enabled', 'category__title', ]
    list_display_links = ['id', 'title', ]
    search_fields = ['id', 'title', 'category', 'enabled', ]
    inlines = [LessonStackedInline]


#~~~~~~~~~~~~~~~~~~~~~~~ Lesson -> Materials ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Lesson)
class LessonAdmin(SortableAdminMixin, admin.ModelAdmin):

    class MaterialStackedInline(SortableStackedInline):
        model = Lesson.materials.through
        extra = 0

    list_display = ['ordering', 'title', 'days',
                    'materials_count', 'related_courses']
    inlines = [MaterialStackedInline]

#~~~~~~~~~~~~~~~~~~~~~~~ Material -> [Components, Attachments] ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(Material)
class MaterialAdmin(SortableAdminMixin, admin.ModelAdmin):

    class ComponentStackedInline(SortableStackedInline):
        model = Material.components.through
        extra = 0

    class AttachmentStackedInline(SortableStackedInline):
        model = Material.attachments.through
        extra = 0

    list_display = ['ordering', 'title',
                    'components_count', 'attachments_count']
    inlines = [ComponentStackedInline, AttachmentStackedInline]


#~~~~~~~~~~~~~~~~~~~~~~~ Others ~~~~~~~~~~~~~~~~~~~~~~~#


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'color', ]
    list_display_links = ['id', 'title', ]
    ordering = ['id', ]


@admin.register(FeaturedCourse)
class FeaturedCourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(MaterialComponent)
class MaterialComponentAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(MaterialAttachment)
class MaterialAttachmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
