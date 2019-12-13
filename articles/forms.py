from django import forms
from . import models

# class meta - defines fields you want and which model they will come from
class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article 
		fields = ['title','slug','body','thumb']