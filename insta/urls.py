from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url('^$',views.news_today,name='newsToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.newimage, name='newimage'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^new/comment/(\d+)',views.newcomment, name='newcomment'), 
    url(r'^like/(\d+)', views.like, name='like'),
    url(r'^follow/(\d+)', views.follow, name='follow'),
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)