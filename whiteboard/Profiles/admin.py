from django.contrib import admin

from .models import Major, Minor, StudentUser, Department, Professor

admin.site.register(Major)
admin.site.register(Minor)
admin.site.register(StudentUser)
admin.site.register(Department)
admin.site.register(Professor)
