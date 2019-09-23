from django.contrib import admin
from dashboard.models import AdModel, CityModel,CommentModel
# Register your models here.

admin.site.register(AdModel)
admin.site.register(CityModel)
admin.site.register(CommentModel)