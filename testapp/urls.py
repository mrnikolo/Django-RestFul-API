from django.urls import path
from .views import homeapi

urlpatterns = [
    path('testapi' , homeapi )

]