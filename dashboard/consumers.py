import json
from channels.generic.websocket import WebsocketConsumer
from .models import Payment, Subscriber
from django.contrib.auth.models import User
from decimal import Decimal


class PaymentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected'
        }))

    def receive(self, text_data):
        data_json = json.loads(text_data)

        if not data_json:
            return None

        event_data = data_json['eventData']

        if data_json['event'] == 'Delete Payment':
            payment_id = event_data['payment_id']
            subscriber = Subscriber.objects.filter(
                pk=event_data['subscriber_id']).first()
            payment = Payment.objects.filter(pk=payment_id).first()

            if payment.manager == self.scope['user']:
                payment.delete()
                subscriber.debt += payment.paid_amount
                subscriber.save()
            elif payment.manager != self.scope['user']:
                self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': 'Manager does not match'
                }))

        elif data_json['event'] == 'Create Payment':
            subscriber = Subscriber.objects.filter(
                name=event_data['subscriber']).first()
            paid_amount = event_data['paid_amount']
            manager = User.objects.filter(
                username=event_data['manager']).first()
            payment = Payment(subscriber=subscriber,
                              paid_amount=paid_amount, manager=manager)
            payment.save()
            subscriber.debt -= Decimal(payment.paid_amount)
            subscriber.save()
