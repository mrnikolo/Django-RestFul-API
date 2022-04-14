from django.shortcuts import get_object_or_404, render
from project import models
from django.views import generic
from django.urls import reverse_lazy

from rest_framework.decorators import api_view
from .models import Blog
from rest_framework.response import Response
from .serializer import BlogSerializer

from project.models import Blog

from django.core.paginator import Paginator


# class BlogView(generic.ListView):
#     model = Blog


# class BlogCreateView(generic.CreateView):
#     model = Blog
#     fields = "__all__"

#     success_url = reverse_lazy("createblog")






class singleView(generic.ListView):
    model = Blog


@api_view(['GET'])
def api_blog(request):
    blogs = Blog.objects.all()
    blog_serializer = BlogSerializer(blogs, many = True)
    return Response(blog_serializer.data) 


@api_view(['GET'])
def blog_details(request , pk ):
    blog = Blog.objects.get(id = pk)
    blog_serializer = BlogSerializer(blog, many = False)
    return Response(blog_serializer.data) 


@api_view(['Post'])
def blog_Save(request ):

    blog = BlogSerializer(data=request.data)

    if blog.is_valid():
        blog.save()

        return Response(blog.data)

@api_view(['Post'])
def blog_Update(request, pk):
    instance = Blog.objects.get(id = pk)
    blog = BlogSerializer(instance=instance , data=request.data)

    if blog.is_valid():
        blog.save()

        return Response(blog.data)

@api_view(['DELETE'])
def blog_Delete(request, pk):

    instance = Blog.objects.get(id = pk)
    instance.delete()


    return Response('Blog Deleted!')






# # Create your views here.
# def detiles(request, pk):
#     post = get_object_or_404(models.Blog,id=pk)
#     context={'post':post}
#     return render(request, 'detiles.html', context)

   
    

def blog(request):
    blogs=Blog.objects.order_by('-creat_at')
    paginator = Paginator(blogs, 1)

    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    contaxt={'blogs':blogs}
    return render(request ,'blog.html', contaxt)


    
# def contact(request):
#     return render(request ,'contact.html')

# def home(request):

#     return render(request , 'home.html')

    

# def about(request):
#     return render(request ,'about.html')


