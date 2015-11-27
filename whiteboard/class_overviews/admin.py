from django.contrib import admin
from .models import Course, Section, Document, Semester


class Sections(admin.StackedInline):
    model = Section
    extra = 1
    

class CourseAdmin(admin.ModelAdmin):
    inlines = [Sections]
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Document)
admin.site.register(Semester)

