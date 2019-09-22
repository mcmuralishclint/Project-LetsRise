from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from blog.models import BlogModel
# Create your views here.
def bloghome(request):
	blogs = BlogModel.objects.all()
	blogs_paginator = Paginator(blogs,1)
	page = request.GET.get('page')
	blogs = blogs_paginator.get_page(page)

	context={
	'blogs':blogs
	}
	return render(request,'blog/bloghome.html',context)

def blogdetail(request,id):
	blog = BlogModel.objects.get(id = id)
	context={
	'blog':blog
	}
	return render(request,'blog/blogdetail.html',context)