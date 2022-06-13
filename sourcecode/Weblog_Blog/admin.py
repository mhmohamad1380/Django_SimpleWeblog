from django.contrib import admin

# Register your models here.
from Weblog_Blog.models import BlogContent, Category, Sidebar, SocialMedias, FooterInfo


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'active_or_not']


admin.site.register(BlogContent, BlogAdmin)
admin.site.register(Category)
admin.site.register(Sidebar)
admin.site.register(SocialMedias)
admin.site.register(FooterInfo)
