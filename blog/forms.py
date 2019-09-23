from django import forms
from tinymce import TinyMCE
from blog.models import BlogCommentModel,BlogModel

class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = BlogCommentModel
		fields = ['comment']

class BlogForm(forms.ModelForm):
	content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
	class Meta:
		model = BlogModel
		exclude = ['user','comments','featured']