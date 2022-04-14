from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    path('api_blog',views.api_blog, name='api_blog'),
    path('api_blog/details/<pk>',views.blog_details, name='blog_details'),
    path('api_blog/save',views.blog_Save, name='blog_Save'),
    path('api_blog/update/<pk>',views.blog_Update, name='blog_Update'),
    path('api_blog/delete/<pk>',views.blog_Delete, name='blog_Delete'),




    path('blog/<int:pk>',views.detiles, name='detiles'),
    path('contact',views.contact, name='contact'),
    path('blog',views.blog, name='blog'),



    path('blogview' , views.BlogView.as_view() , name='blogview'),
    path('createblog' , views.BlogCreateView.as_view() , name='createblog'),



    path('about',views.about, name='about'),
    ]