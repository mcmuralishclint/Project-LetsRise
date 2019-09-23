from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from blog.models import BlogModel,BlogCommentModel
from blog.forms import BlogCommentForm,BlogForm
from django.db.models import Q #Search
from datetime import datetime
# Create your views here.
def bloghome(request):
	blogs = BlogModel.objects.all()
	all_comments = BlogCommentModel.objects.all()
	all_blogs = BlogModel.objects.all()[:5]
	blogs_paginator = Paginator(blogs,2)
	page = request.GET.get('page')
	blogs = blogs_paginator.get_page(page)

	context={
	'blogs':blogs,
	'all_blogs':all_blogs,
	'all_comments':all_comments,
	}
	return render(request,'blog/bloghome.html',context)

def blogdetail(request,id):
	all_comments = BlogCommentModel.objects.all()
	#all_comments = all_comments.order_by("-timestamp")[0:5]

	blog = BlogModel.objects.get(id = id)
	comments = BlogCommentModel.objects.filter(blog = id)
	form = BlogCommentForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.instance.user = request.user
			form.instance.blog = blog
			form.instance.timestamp = datetime.now()
			form.save()

			blog.comments = blog.comments+1
			blog.save()
			form = BlogCommentForm()

	context={
	'blog':blog,
	'comments':comments,
	'form':form,
	'no_of_comments':len(comments),
	'all_comments':all_comments,
	}
	return render(request,'blog/blogdetail.html',context)



def delete_blog(request,id):
	blog = get_object_or_404(BlogModel,id=id)
	blog.delete()
	return redirect('/blog/')



def edit_blog(request,id):
	blog = get_object_or_404(BlogModel,id=id)
	form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
	if request.method=="POST":
		if form.is_valid():
			form.instance.user=request.user
			form.save()
			return redirect('/blog/')


	context={
	'form':form,
	'heading':'Edit your post',
	'subheading':'Edit and Update your post',
	}
	return render(request,'blog/create_blog.html',context)

def create_blog(request):
	form = BlogForm(request.POST or None, request.FILES or None)
	if request.method=="POST":
		if form.is_valid():
			form.instance.user=request.user
			form.instance.featured=0
			form.instance.comments=0
			form.save()
			return redirect('/blog/')
	context={
	'form':form,
	'heading':'Create a blog post',
	'subheading':'Engage with our community'
	}
	return render(request,'blog/create_blog.html',context)



def search_result(request):
	blogs=''
	search_id = request.GET.get('q')		#Keyword Search
	
	blogs = BlogModel.objects.filter(Q(description__icontains=search_id) | Q(title__icontains=search_id) | Q(content__icontains=search_id))
	all_comments = BlogCommentModel.objects.all()
	if len(blogs)>0:
		blogs_paginator = Paginator(blogs,2)
		page = request.GET.get('page')
		blogs = blogs_paginator.get_page(page)
	else:
		page=0
	#blogs = blogs.objects.all()[:1]
	context={
			'search_id':search_id,
			'search':'search',
			'blogs':blogs,
			'no_of_blogs':len(blogs),
			'page':page,
			'all_blogs':BlogModel.objects.all(),
			'all_comments':all_comments,
			'no_of_comments':len(all_comments),
			}	
	return render(request, 'blog/bloghome.html',context)