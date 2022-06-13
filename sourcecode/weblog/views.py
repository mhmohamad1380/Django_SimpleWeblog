
from django.shortcuts import render

from Weblog_Blog.models import BlogContent, Category, Sidebar, SocialMedias


def sidebar(request, *args, **kwargs):
    category: Category = Category.objects.all()
    side_bar = Sidebar.objects.first()
    social = SocialMedias.objects.all()
    context = {
        'category': category,
        'sidebar': side_bar,
        'social': social,
    }
    return render(request, 'base/sidebar.html', context)
