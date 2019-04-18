"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from blog.views import PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView
from config.views import LinkView
from comment.views import CommentView
from blog.rss import LatestPostFeed
from blog.apis import PostViewSet, CategoryViewSet
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from .settings.base import STATIC_ROOT

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 首页
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),   # 分类页面
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),     # 标签
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkView.as_view(), name='links'),  # 友链
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss/$', LatestPostFeed(), name='rss'),

    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', xadmin.site.urls, name='xadmin'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),    # 分类搜索自动补全
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),     # 标签搜索自动补全
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
