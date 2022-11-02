from django.contrib.auth import logout
from django.views.generic.base import TemplateView

from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import Subscriber, Payment

# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self,*args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args,**kwargs)
        context['payments'] = Payment.objects.all()
        return context

class SubscribersView(TemplateView):
    template_name = "subscribers.html"

def LogoutView(request):
    logout(request)
    # Redirect to a success page.

@receiver(post_save, sender=Payment)
def UpdateTotalPayed(sender, instance, **kwargs):
    subscriber = Subscriber.objects.get(id=instance.subscriber.id)
    subscriber.zaplatene_dokopy += instance.platba_suma
    subscriber.save()

request_finished.connect(UpdateTotalPayed, dispatch_uid="my_unique_identifier")
