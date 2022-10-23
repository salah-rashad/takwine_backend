from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.courses.models.course import Course

from apps.courses.models.lesson import Lesson
from apps.users.intermediates import Rel_Enrollment_Lesson

from .forms import UserChangeForm, UserCreationForm
from .models import Enrollment, User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display_links = ['email']
    list_display = ['id', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_active']
    list_filter = ['gender', 'is_superuser',
                   'is_staff', 'is_active', 'city', 'job']
    fieldsets = [
        ['General', {
            'fields': ['email', 'password', 'first_name',
                       'last_name', 'birthDate', 'imageUrl',
                       'phoneNumber', 'city', 'job', 'gender']
        }],
        ['Permissions', {
            'fields': ['is_active', 'is_superuser', 'is_staff']
        }],
    ]
    add_fieldsets = [
        ['General', {
            'classes': ['wide', ],
            'fields': ['email', 'password1', 'password2', 'birthDate']
        }],
        ['Optional', {
            'classes': ['wide', ],
            'fields': ['first_name', 'last_name', 'imageUrl', 'phoneNumber', 'city', 'job', 'gender']
        }],
        ['Permissions', {
            'fields': ['is_active', 'is_staff']
        }],
    ]
    search_fields = ['id', 'email', 'first_name', 'last_name']
    ordering = ['id']


class LessonInline(admin.TabularInline):
    model = Enrollment.completeLessons.through
    extra = 0

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'lesson':
            if request.course_id is not None:
                field.queryset = Course.objects.filter(
                    id=request.course_id).get().lessons
            else:
                field.queryset = field.queryset.none()

        return field


# class MaterialInline(admin.TabularInline):
#     model = Enrollment.completeMaterials.through


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'created_at', 'progress']
    list_filter = ['created_at', 'user', 'course__title']
    list_display_links = ['user', 'course', ]
    ordering = ['id', ]
    inlines = [LessonInline,
               #    MaterialInline
               ]
    fieldsets = [
        [None, {
            "fields": ['user', 'course', 'currentLesson', 'currentMaterial', 'created_at', 'updated_at']
        }]
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('user', 'course', 'currentLesson', 'currentMaterial')
        return self.readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        if obj:
            request.course_id = obj.course.id
        else:
            request.course_id = None
        return super().get_form(request, obj, **kwargs)
