
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from user.views import signup

app_name = 'user'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), #Login, Logout
    path('signup/', signup.as_view(), name='signup'),
    
] 