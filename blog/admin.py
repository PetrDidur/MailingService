from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'views_count',)
    list_filter = ('views_count',)
    search_fields = ('title', 'body',)
