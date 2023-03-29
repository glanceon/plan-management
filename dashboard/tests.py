import datetime
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from dashboard.models import Service, PayingGroup, Subscriber, Payment

# Every Model here is joined


class GeneralModelTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        user = User.objects.create(
            username="TestUser", password="VeryComplexFakePassword123[[]]")
        service = Service.objects.create(
            service_name="netflix", whole_service_name="Netflix", manager=user)
        group = PayingGroup.objects.create(
            group_name="My Netflix Group 1", monthly_cost="2", service=service, manager=user
        )
        subscriber = Subscriber.objects.create(
            name="Felix", iban="NL61RABO4110487447", debt="0", manager=user
        )
        subscriber.group.add(group)
        date = datetime.date(year=2023, month=3, day=29)
        Payment.objects.create(
            subscriber=subscriber, date_of_payment=date, paid_amount="4", manager=user
        )

    def test_service_created(self):
        self.assertEqual(Service.objects.get(
            id=1).__str__(), 'Netflix')

    def test_group_created(self):
        self.assertEqual(PayingGroup.objects.get(
            id=1).__str__(), 'My Netflix Group 1')

    def test_subscriber_created(self):
        self.assertEqual(Subscriber.objects.get(
            id=1).__str__(), 'Felix')

    def test_payment_created(self):
        self.assertEqual(Payment.objects.get(
            id=1).__str__(), 'Felix 4.00€ 2023-03-29')
