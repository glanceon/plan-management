import json
from channels.generic.websocket import WebsocketConsumer
from .models import Payment, Subscriber


class PaymentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected'
        }))

    def receive(self, text_data):
        data_json = json.loads(text_data)
        changed_payment_sub = data_json['changed_payment_sub']
        changed_payment_id = data_json['changed_payment_id']
        payment = Payment.objects.get(pk=changed_payment_id)
        subscriber = Subscriber.objects.get(name=changed_payment_sub)
        payment.subscriber = subscriber
        payment.save()

        print(changed_payment_sub, changed_payment_id)
