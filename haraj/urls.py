"""haraj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from haraj_app import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', views.index),
    path ('contact/', views.contact),
    path('add/', views.add),
    path('detalis/', views.detalis)
    
=======
    path('admin/', admin.site.urls,),
    path('', views.index,name='home'),
    path ('contact/', views.contact,name='contact'),
    path('add/', views.add,name='add'),
>>>>>>> 3a51316435853acc6171c3857478a2f621ae376d
    ]
