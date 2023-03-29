import decimal
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

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        if not self.request.user.is_authenticated:
            return context
        context['payments'] = Payment.objects.defer(
            'manager').filter(manager=self.request.user)
        context['services'] = Service.objects.defer(
            'manager').filter(manager=self.request.user)
        context['subscriber'] = Subscriber.objects.defer('manager').filter(
            manager=self.request.user)
        return context


def LogoutView(request):
    logout(request)
    # Redirect to a success page.


@receiver(post_save, sender=Payment)
def UpdateDebt(sender, instance, **kwargs):
    subscriber = Subscriber.objects.filter(id=instance.subscriber.id).first()
    subscriber.debt -= instance.paid_amount
    subscriber.save()
