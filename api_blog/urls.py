from django.urls import path
from .views import blogapi

urlpatterns = [
    path('blogsapi' , blogapi)

]