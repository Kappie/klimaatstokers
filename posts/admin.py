from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
from .models import Post



class PostAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Post, PostAdmin)


