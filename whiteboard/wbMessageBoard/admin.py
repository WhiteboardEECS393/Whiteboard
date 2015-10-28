from django.contrib import admin
from .models import DiscussionBoard, Thread, Post
# Register your models here.

admin.site.register(DiscussionBoard)

class PostInLine(admin.StackedInline):
    model = Post
    extra = 1

class ThreadAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Thread Content', {'fields':['subject', 'creator', 'message']}),
        ("Date Information", {'fields':['time_of_creation']}),
        ("Board", {'fields' : ['board']}),

    ]
    inlines = [PostInLine]

admin.site.register(Thread, ThreadAdmin)
#admin.site.register(Post)