from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'enrollment_date', 'active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('active', 'enrollment_date')
