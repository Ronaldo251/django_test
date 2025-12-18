from django.contrib import admin
from .models import Student, Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'active', 'is_free')
    list_filter = ('active', 'enrollment_date', 'is_free')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    readonly_fields = ('is_free',)