from django.conf.urls import url
from usermodel import views

urlpatterns = [
	url(r'^(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify'),
]
