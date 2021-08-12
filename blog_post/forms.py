from django import forms
from .models import *


class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = BlogComment
		fields = ('message',)