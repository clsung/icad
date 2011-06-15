"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.utils import unittest
from django.db.utils import *
from ads.models import *


class DeviceTest(TestCase):
    def setUp(self):
        pass
    def test_no_geotag_creation(self):
        with self.assertRaises(DatabaseError) as cm:
            tagh = Device.objects.create(imei = '355195000000017',
                    model = 'S710e')
    def test_basic_creation(self):
        sinica = Point.objects.create(lat = 25.0392, lon = 121.5250)
        tagh = Device.objects.create(imei = '355195000000017',
                model = 'S710e', location = sinica)
        self.assertEqual(tagh.model, "S710e")



