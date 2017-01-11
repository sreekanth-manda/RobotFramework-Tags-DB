from django.conf.urls import include, url
from django.contrib import admin
from tags_app.views import main_page, tagging_main_page, get_tag_list, get_tags_info, select_tags
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'tags_db_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$|home_page', main_page),
    url(r'^tagging|home$', tagging_main_page),
    url(r'^(all|\w)/$', get_tag_list),
    url(r'^select_tag_with_(all|\w)/$', select_tags),
    url(r'^get_tag_(\w+)/$', get_tags_info),
    url(r'^admin/', include(admin.site.urls)),
]
