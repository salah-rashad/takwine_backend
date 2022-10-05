from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, EnrolledCourse


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display_links = ['email']
    list_display = ('id', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_active',)
    list_filter = ('gender', 'is_superuser',
                   'is_staff', 'is_active', 'city', 'job', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
         'last_name', 'city', 'job', 'gender',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('id', 'email', 'first_name', 'last_name',)
    ordering = ('id',)


class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', )
    list_filter = ('id', 'user', 'course__id',)
    ordering = ('id', )


admin.site.register(User, UserAdmin)
admin.site.register(EnrolledCourse, UserCourseProgressAdmin)
