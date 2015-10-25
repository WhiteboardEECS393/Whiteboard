from django.contrib import admin

from .models import BasicUser, Major, Minor, StudentUser, Department, TeachingAssistantUser, ProfessorUser

admin.site.register(BasicUser)
admin.site.register(Major)
admin.site.register(Minor)
admin.site.register(StudentUser)
admin.site.register(Department)
admin.site.register(TeachingAssistantUser)
admin.site.register(ProfessorUser)
