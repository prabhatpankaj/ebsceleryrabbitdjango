from django.conf.urls import url
from blog import views

urlpatterns = [
	url(r'^(?P<slug>[a-zA-Z0-9\-]+)', views.view_post, name='view_post'),
]
