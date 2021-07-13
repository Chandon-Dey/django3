from django.urls import path,include
from . import views

app_name = 'Blog'

urlpatterns = [
    path('',views.blog,name='blog'),

    path('blog/<slug>/',views.blog_details,name='blog_details')
]