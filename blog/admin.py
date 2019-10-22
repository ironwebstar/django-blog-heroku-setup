from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'updated_at', 'image', 'image_tag', )
    readonly_fields = ('image_tag', 'created_at', 'updated_at')


admin.site.register(Blog, BlogAdmin)
