from django.contrib import admin
from .models import Posts, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    
    inlines = [
        CommentInline,
    ]
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Posts, PostAdmin)
admin.site.register(Comment)