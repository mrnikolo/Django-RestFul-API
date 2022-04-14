from django.shortcuts import render , redirect
import requests
import json
from django.http import response

# Create your views here.

def blogapi(request):
    response = requests.get("http://127.0.0.1:8000/project/api_blog").json()
    context = {
        "blogs" : response
        }
    return render(request , 'api_blog/blogsapi.html' , context)

