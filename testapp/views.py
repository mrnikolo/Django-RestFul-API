from django.shortcuts import render 
import json
import requests
from django.http import response


# Create your views here.
def homeapi(request):
    blogs = request.get("http://127.0.0.1:8000/project/api_blog").json()
    context = {
        "blogs" : blogs
    }
    return render(request , 'testapp/apihome.html' , context)

