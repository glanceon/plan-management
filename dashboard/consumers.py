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
        if data_json['payment_id']:
            payment_id = data_json['payment_id']
            payment = Payment.objects.filter(pk=payment_id).first()
            payment.delete()
