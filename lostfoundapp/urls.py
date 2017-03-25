from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'viewnotices',views.view_all_notices,name = 'view_all_notices'),
    url(r'createnotice',views.create_notice,name = 'createnotice'),
    url(r'deletenotice', views.delete_notice, name = 'deletenotice'),
    url(r'updatenotice', views.update_notice, name = 'update_notice')
    ]