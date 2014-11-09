from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from teams import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'members', views.MemberViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('login.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^level/', include('levels.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))

)
