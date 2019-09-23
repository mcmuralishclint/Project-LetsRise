from django.urls import path
from blog.views import bloghome,blogdetail,delete_blog,edit_blog,create_blog,search_result
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('',bloghome,name='bloghome'),
    path('blog-detail/<id>',blogdetail,name='blogdetail'),
    path('create_blog/',create_blog,name='create_blog'),
    path('edit_blog/<id>',edit_blog,name='edit_blog'),
    path('delete_blog/<id>',delete_blog,name='delete_blog'),
    path('search-result/',search_result,name='search_result'),
]
