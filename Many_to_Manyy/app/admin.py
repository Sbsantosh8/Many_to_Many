from django.contrib import admin
from .models import Student, Course

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "get_students")


    def get_students(self, obj):
        return ", ".join([student.name for student in obj.students.all()])

    get_students.short_description = "Students"  # Optional: custom column header


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
