from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from feedback import app_settings
from feedback import models
from django.core import mail

class FeedbackTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('testuser', 'test@example.com', 'testpw')

    def test_email(self):
        app_settings.FEEDBACK_SEND_MAIL=True
        feedback = models.Feedback(
                feedback='test feedback',
                path='/',
                )
        feedback.save()
        self.assertEqual(len(mail.outbox),1)

        app_settings.FEEDBACK_SEND_MAIL=False
        feedback = models.Feedback(
                feedback='another test feedback',
                path='/other/path/',
                )
        feedback.save()
        self.assertEqual(len(mail.outbox),1)


    def tearDown(self):
        pass
