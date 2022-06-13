from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from weblog.views import sidebar
from Weblog_Blog.views import blog_detail, HomePage, BlogSearch, Footer, BlogView

urlpatterns = [
    path('', HomePage.as_view()),
    path('footer', Footer, name='footer'),
    path('blogs', BlogView),
    path('blogs/', BlogView),
    path('blogs/<blogID>/<blogTitle>', blog_detail),
    path('blog/<category>', sidebar),
    path('search', BlogSearch.as_view()),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
