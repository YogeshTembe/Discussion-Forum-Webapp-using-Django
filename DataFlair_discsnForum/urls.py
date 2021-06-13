from django.contrib import admin
from django.urls import path
from Discussion_Forum.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='Home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]