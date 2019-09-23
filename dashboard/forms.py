from django import forms
from tinymce import TinyMCE
from dashboard.models import AdModel,CommentModel


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class AdForm(forms.ModelForm):
	description = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
	class Meta:
		model = AdModel
		exclude = ['user','comments','total_rating','featured']

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentModel
		fields = ['comment','rating']
