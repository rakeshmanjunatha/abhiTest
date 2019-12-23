"""fsc_batch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('checklist/', check_list, name="check_list"),
    path('view_checklist/', view_checklist, name="view_checklist"),
    path('create_fsc_batch/', create_fsc_batch, name="create_fsc_batch"),
    path('send_fsc_mail/', send_fsc_mail, name="send_fsc_mail"),
]
