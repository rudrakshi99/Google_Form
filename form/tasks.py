from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task




@shared_task(bind=True)
def send_email(self, email):
    mail_subject = "Conformation"
    message = "Your contact info gets recorded."
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False
    )
    return "Done"


    
    