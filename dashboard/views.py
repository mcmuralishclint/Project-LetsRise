from django.shortcuts import render,redirect,get_object_or_404
from dashboard.models import AdModel,CityModel,CommentModel
from blog.models import BlogModel
from django.core.paginator import Paginator
import operator #Search
from django.db.models import Q #Search
from dashboard.forms import AdForm,CommentForm
from datetime import datetime
from django.contrib.auth.models import User	

def index(request):
	ads = AdModel.objects.filter(featured=1)
	blogs = BlogModel.objects.filter(featured=1)
	cities = CityModel.objects.all()
	#category filter
	marketing = len(AdModel.objects.filter(category="Marketing"))
	sc = len(AdModel.objects.filter(category="Student Consultancy"))
	wd = len(AdModel.objects.filter(category="Web Development"))
	teach = len(AdModel.objects.filter(category="Teach"))
	design = len(AdModel.objects.filter(category="Designing"))
	other = len(AdModel.objects.filter(category="Other"))


	context={
	'ads':ads,
	'marketing':marketing,
	'sc':sc,
	'wd':wd,
	'teach':teach,
	'design':design,
	'other':other,
	'blogs':blogs,
	'cities':cities,
	}
	return render(request,'dashboard/index.html',context)

def ad_detail(request,id):
	ad = AdModel.objects.get(id=id)
	comments = CommentModel.objects.filter(ad = id)
	comment_form = CommentForm(request.POST or None)
	if request.method=="POST":
		if comment_form.is_valid():
			comment_form.instance.user=request.user
			comment_form.instance.ad = ad
			comment_form.instance.timestamp = datetime.now()
			comment_form.save()


			ad.comments = ad.comments+1
			ad.total_rating = ad.total_rating + int(comment_form.instance.rating)
			ad.save()


	context = {
	'ad':ad,
	'comments':comments,
	'no_of_comments':len(comments),
	'form':comment_form,
	}
	return render(request,'dashboard/ad_detail.html',context)

def ads(request):
	ads = AdModel.objects.all()
	ads_paginator = Paginator(ads,2)
	page = request.GET.get('page')
	ads = ads_paginator.get_page(page)
	#ads = ads_paginator.get_page(page)
	context={
	'ads':ads,
	}
	return render(request,'dashboard/ads.html',context)



def search_result(request):
	ads=''
	search_id = request.GET.get('q')		#Keyword Search
	search_category = request.GET.get('qcategory')		#Keyword Search

	context={
			'search':'search',
			'categories':'categories',
			'ads':'ads',
			}




	try:
		ads = AdModel.objects.filter(Q(description__icontains=search_id) | Q(title__icontains=search_id))
		context={
			'search_id':search_id,
			'search':'search',
			'ads':ads
			}
	except:
		pass


	try:
		categories = AdModel.objects.filter(Q(category__icontains=search_category))
		context={
			'search_id':search_category,
			'search':'search',
			'ads':categories
			}
	except:
		pass


	
	return render(request, 'dashboard/ads.html',context)



def create_ad(request):
	form = AdForm(request.POST or None, request.FILES or None)
	if request.method=="POST":
		if form.is_valid():
			print('pass')
			form.instance.user=request.user
			form.save()
			return redirect('/ads/')

	context={
	'form':form,
	'heading':'Create an Ad',
	'subheading':'Create an Ad for your company',
	}
	return render(request,'dashboard/create_ad.html',context)


def edit_ad(request,id):
	ad = get_object_or_404(AdModel,id=id)
	form = AdForm(request.POST or None, request.FILES or None, instance=ad)
	if request.method=="POST":
		if form.is_valid():
			form.instance.user=request.user
			form.save()
			return redirect('/ads/')


	context={
	'form':form,
	'heading':'Edit your Ad',
	'subheading':'Edit and Update your ad',
	}
	return render(request,'dashboard/create_ad.html',context)


def delete_ad(request,id):
	ad = get_object_or_404(AdModel,id=id)
	ad.delete()
	return redirect('/ads/')


