import logging

from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celerydjango.celery import app
 
@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        subject = 'Verify your enopits account'
        verification_message = 'Follow this link to verify your account: ' 'http://%s%s'% (settings.DOMAIN_NAME,reverse('verify', kwargs={'uuid': str(user.verification_uuid)}))
        from_email = settings.DEFAULT_EMAIL_USER
        to_email = [user.email]
        send_mail(
            subject,
            verification_message,
            from_email,
            to_email,
            fail_silently=True,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
