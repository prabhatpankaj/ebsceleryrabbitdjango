from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celerydjango.celery import app
from .models import Post
from django.conf import settings
 
REPORT_TEMPLATE = """
Here's how you did till now:
{% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |
{% endfor %}
"""
 
@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue

        subject = 'Number of post views'
        template = Template(REPORT_TEMPLATE)
        from_email = settings.DEFAULT_EMAIL_USER
        to_email = [user.email]
        send_mail(
            subject,
            template.render(context=Context({'posts': posts})),
            from_email,
            to_email,
            fail_silently=True,
        )