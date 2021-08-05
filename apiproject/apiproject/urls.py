"""apiproject URL Configuration

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
from blogs.views.fn_based_view import (get_blogs,create_blogs,update_blogs, get_blogs1,delete_blog)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs', csrf_exempt(get_blogs)),
    path('blogs1', csrf_exempt(get_blogs1)),
    path('blogs/create',csrf_exempt(create_blogs)),
    path('blogs/update',csrf_exempt(update_blogs)),
    path('blogs/delete',csrf_exempt(delete_blog)),
]
