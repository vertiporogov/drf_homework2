from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Subscription, Course
from materials.serializers.subscription import SubscriptionSerializer


class SubscriptionView(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        queryset = Course.objects.all()
        course_item = get_object_or_404(queryset, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка на курс удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка на курс добавлена'

        return Response({"message": message})
