from django import forms
from blog.models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'author', 'description', 'image')

	# def __init__(self, *args, **kwargs):
	# 	super(BlogForm, self).__init__(*args, **kwargs)
	# 	for field in self.fields:
	# 		self.fields[field].widget.attrs['class'] = 'form-control'
