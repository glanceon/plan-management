from django.contrib import admin
from dashboard.models import Service, Subscriber, Payment, PayingGroup
# Register your models here.

admin.site.register(Service)
admin.site.register(Subscriber)
admin.site.register(Payment)
admin.site.register(PayingGroup)
