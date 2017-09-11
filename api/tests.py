from django.test import TestCase
from .models import Parent
from .models import Son
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
"""
class ModelTestCase(TestCase):
    def setUp(self):
        self.son_name = "Roman"
        self.son_lastName = "Aguilar"
        self.son_mail= "donromi@synegra.com"
        self.son_password = "RomiGomitas"
        self.son_cellphone = "2711500099"
        self.son = Parent(name=self.son_name)
        self.son = Parent(name=self.son_lastName)
        self.son = Parent(name=self.son_mail)
        self.son = Parent(name=self.son_password)
        self.son = Parent(name=self.son_cellphone)

    def test_model_can_create_a_son(self):
        old_count = Parent.objects.count()
        self.son.save()
        new_count = Parent.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """"""Api views tests."""
"""
    def setUp(self):
        parentUser = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user=parentUser)
        self.son_data = {'name': 'Roman', 'lastName' : 'Aguilar', 'mail' : 'donromi@synegra.com', 'password' : 'RomiGomitas', 'cellphone' : '2222222222'}
        self.response = self.client.post(
            reverse('create'),
            self.son_data,
            format="json")

    def test_api_can_create_a_son(self):
        """"""Checks that sons are created correctly.""""""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
"""
