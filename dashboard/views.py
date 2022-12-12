from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import Subscriber, Payment, Service

# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"
    def get_context_data(self,*args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args,**kwargs)
        context['payments'] = Payment.objects.all()
        context['service'] = Service.objects.all()
        context['subscriber'] = Subscriber.objects.all()
        return context

def LogoutView(request):
    logout(request)
    # Redirect to a success page.

@receiver(post_save, sender=Payment)
def UpdateTotalPayed(sender, instance, **kwargs):
    subscriber = Subscriber.objects.get(id=instance.subscriber.id)
    return print(subscriber.meno)

