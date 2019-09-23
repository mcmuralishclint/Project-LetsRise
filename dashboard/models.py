from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import HTMLField
# Create your models here.
class CityModel(models.Model):
	city = models.CharField(max_length=50)
	def __str__(self):
		return self.city
	
class AdModel(models.Model):
	CATEGORY = (
        ('Marketing', 'Marketing'),
        ('Student Consultancy', 'Student Consultancy'),
        ('Web Development', 'Web Development'),
        ('Teach', 'Teach'),
        ('Designing', 'Designing'),
        ('Other', 'Other'),
    )
	title = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	category = models.CharField(max_length=50, choices=CATEGORY, default='Other')
	description = HTMLField('Content')
	image = models.ImageField(upload_to = 'img/ad_image',blank=False)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	city = models.ForeignKey(CityModel,on_delete = models.CASCADE, default = "")
	featured = models.BooleanField(default=0)
	comments = models.IntegerField(default=0)
	total_rating = models.IntegerField(default=0)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('dashboard:ad_detail', kwargs={
            'id': self.id
        })

class CommentModel(models.Model):
	CATEGORY = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	ad = models.ForeignKey(AdModel,on_delete=models.CASCADE)
	comment = models.TextField()
	rating = models.CharField(max_length=1, choices=CATEGORY, default='3')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user) + '-' + str(self.ad)


