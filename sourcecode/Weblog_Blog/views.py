import itertools

from django import views
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from django.views.generic import ListView

from Weblog_Blog.models import BlogContent, FooterInfo
import sys
import urllib


class HomePage(ListView):
    template_name = 'homepage.html'
    paginate_by = 12

    def get_queryset(self):
        return BlogContent.object.get_active_blogs().all()


def BlogView(request):

    blogs = BlogContent.object.get_active_blogs().all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 16)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        'blogs': pages,
    }
    return render(request, 'blogs.html', context)


def Footer(request):
    blogs = BlogContent.object.get_active_blogs().all()[:4]
    footer = FooterInfo.objects.first()

    def mygrouper(n, iterable):
        args = [iter(iterable)] * n
        return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

    context = {
        'blogs': mygrouper(4, blogs),
        'footer': footer

    }
    return render(request, 'base/footer.html', context)


def blog_detail(request, *args, **kwargs):
    selected_blog_id = kwargs['blogID']
    blog_de: BlogContent = BlogContent.object.filter(id=selected_blog_id).first()
    myList = []
    category = ""
    for c in blog_de.category.all():
        myList.append(c)
    for ca in myList:
        category += '/' + str(ca) + '/'

    context = {
        'blog': blog_de,
        'category': category
    }
    return render(request, 'blog_detail.html', context)


class BlogSearch(ListView):
    template_name = 'homepage.html'
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        print(BlogContent.object.Search(query))
        if query is not None:
            return BlogContent.object.Search(query)
        else:
            return BlogContent.object.get_active_blogs()


def handler_404(request, exception):
    return render(request, 'base/404.html', {})
