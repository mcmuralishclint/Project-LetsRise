from django.urls import path
from blog.views import bloghome,blogdetail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('',bloghome,name='bloghome'),
    path('blog-detail/<id>',blogdetail,name='blogdetail')
]
