from celery import shared_task
from django.conf import settings

from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def course_update(course_pk):
    subscriptions = Subscription.objects.filter(course_id=course_pk)
    for s in subscriptions:
        if s.status:
            send_mail(
                subject="Обновление курса",
                message=f'Курс {s.course.name} обновлен',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[s.user.email],
                fail_silently=False
            )
