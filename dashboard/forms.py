from django import forms
from dashboard.models import AdModel,CommentModel

class AdForm(forms.ModelForm):
	class Meta:
		model = AdModel
		exclude = ['user']

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentModel
		fields = ['comment','rating']
