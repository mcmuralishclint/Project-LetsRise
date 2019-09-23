from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import HTMLField
# Create your models here.
class BlogModel(models.Model):
	CATEGORY = (
        ('Marketing', 'Marketing'),
        ('Student Consultancy', 'Student Consultancy'),
        ('Web Development', 'Web Development'),
        ('Teach', 'Teach'),
        ('Designing', 'Designing'),
        ('Other', 'Other'),
    )
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'blog/',blank=False)
	description = models.CharField(max_length=100)
	content = HTMLField('Content')
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=50, choices=CATEGORY, default='Other')
	featured = models.BooleanField(default=0)
	comments = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('dashboard:blog-detail', kwargs={
            'id': self.id
        })

class BlogCommentModel(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user) + '-' + str(self.blog)


