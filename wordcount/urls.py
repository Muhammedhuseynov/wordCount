
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainPage,name='mainPage'),
    path('countResult/',views.countedPage,name='count'),
    path('aboutPage/',views.aboutPage,name='about')

]
