from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import BlogApiView
from weblog.views import sidebar
from Weblog_Blog.views import blog_detail, HomePage, BlogSearch, Footer, BlogView

urlpatterns = [
    path('', HomePage.as_view()),
    path('footer', Footer, name='footer'),
    path('blogs', BlogView.as_view()),
    path('blogs/<blogID>/<blogTitle>', blog_detail),
    path('blog/<category>', sidebar),
    path('search', BlogSearch.as_view()),
    path("api/blog/list", BlogApiView.as_view())
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
