from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from apps.courses.models import Course, CourseCategory, FeaturedCourse, Lesson, Material

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status',)
    list_filter = ('title', 'category', 'status',)
    search_fields = ('id', 'title', 'category', 'status',)
    ordering = ('category', 'title',)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'color', )
    ordering = ('id', )


@admin.register(FeaturedCourse)
class FeaturedCourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
