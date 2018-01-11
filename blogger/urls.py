"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from boards.views import home, about, board_topics, new_topic

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    # url(r'^(?P<username>[\w.@+-]+)/$', user_profile, name='user_profile'),
    # url(r'^about/company/$', about_company, name='about_company'),
    # url(r'^about/author/$', about_author, name='about_author'),
    # url(r'^about/author/vitor/$', about_vitor, name='about_vitor'),
    # url(r'^about/author/erica/$', about_erica, name='about_erica'),
    # url(r'^privacy/$', privacy_policy, name='privacy_policy'),
    url(r'^boards/(?P<pk>\d+)/$', board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
