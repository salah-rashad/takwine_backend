from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.courses.models.course import Course
from apps.courses.models.lesson import Lesson

from .forms import UserChangeForm, UserCreationForm
from .models import (Certificate, CompleteLesson, CourseBookmark,
                     DocumentBookmark, Enrollment, User)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    readonly_fields = ['preview']
    list_display_links = ['email']
    list_display = ['id', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_active']
    list_filter = ['gender', 'is_superuser',
                   'is_staff', 'is_active', 'city', 'job']
    fieldsets = [
        (
            _('Profile Image'),
            {
                'fields': (
                    'preview',
                    'imageUrl',
                )
            }
        ),
        (
            _('General'),
            {
                'fields': (
                    'email',
                    'password',
                    'first_name',
                    'last_name',
                    'birthDate',
                    'phoneNumber',
                    'city',
                    'job',
                    'gender',
                )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ],
            }
        ),
    ]
    add_fieldsets = [
        (
            _('General'),
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'birthDate',
                ),
            }
        ),
        (
            _("Optional"),
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'first_name',
                    'last_name',
                    'imageUrl',
                    'phoneNumber',
                    'city',
                    'job',
                    'gender',
                ),
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            }
        ),
    ]
    search_fields = ['id', 'email', 'first_name', 'last_name']
    ordering = ['id']


class CompleteLessonInline(admin.TabularInline):
    model = CompleteLesson
    extra = 0

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'lesson':
            if request.course is not None:
                field.queryset = Course.objects.filter(
                    id=request.course.id).get().lessons()
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
    inlines = [CompleteLessonInline]
    fieldsets = [
        [None, {
            "fields": ['user', 'course', 'currentLesson', 'created_at', 'updated_at']
        }]
    ]
    readonly_fields = ['user', 'course', 'currentLesson',
                       'created_at', 'updated_at']

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        if obj:
            request.course = obj.course
        else:
            request.course = None
        return super().get_form(request, obj, **kwargs)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseBookmark)
class CourseBookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course']
    list_display_links = ['user', 'course', ]
    pass


@admin.register(DocumentBookmark)
class DocumentBookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'document']
    list_display_links = ['user', 'document', ]
    pass
