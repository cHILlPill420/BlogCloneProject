"""blog_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('blog_app.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    #url(r'accounts/login/$', views.login, name = 'login'),
    path('logout/', LogoutView.as_view( template_name='blog_app/post_list', next_page = '/'), name="logout"),
    #url(r'accounts/logout/$', views.logout, name = 'logout', kwargs = {'next_page':'/'}),
]
