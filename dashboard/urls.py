from django.urls import path
from dashboard.views import index,ad_detail,ads,search_result,create_ad,edit_ad,delete_ad
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'
urlpatterns = [
    path('',index,name='index'),
    path('ad-detail/<id>', ad_detail, name="ad_detail"),
    path('ads/',ads,name='ads'),
    path('search-result/',search_result,name='search_result'),
    path('create_ad/',create_ad,name='create_ad'),
    path('edit_ad/<id>',edit_ad,name='edit_ad'),
    path('delete_ad/<id>',delete_ad,name='delete_ad'),
]

