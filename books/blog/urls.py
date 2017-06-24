from django.conf.urls import url
from blog import views as blog_views
urlpatterns = [
	url(r'^$', blog_views.blogs),
	url(r'^(?P<blog_id>\d+)/$', blog_views.get_blog),
	url(r'create/$', blog_views.create_blog)
]