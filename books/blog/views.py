from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BlogForm

# Create your views here
def blogs(req):
	blogs = Blog.objects.all
	return render(req, 'blogs.html', {'blogs': blogs})

def get_blog(req, blog_id):
	# blog = Blog.objects.get(id=int(blog_id))
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(req, 'blog.html', {'blog': blog})

def create_blog(req):
	form = BlogForm()
	html_form = render_to_string('partial_blog_create.html', {'form': form}, request=req)
	return JsonResponse({'html_form': html_form})