from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from teams import views
from django.views.generic import TemplateView
from leaderboard.views import *

urlpatterns = patterns('',
	
    # Examples:
    url(r'^$', leaderboard),

)
