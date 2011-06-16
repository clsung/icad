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
                model = 'S710e', lat = sinica.lat, lon = sinica.lon)
        self.assertEqual(tagh.model, "S710e")

class SectionTest(TestCase):
    def setUp(self):
#        htc = Point.objects.create(lat = 25.030829, lon = 121.327336)
#        self.tagh = Device.objects.create(imei = '355195000000017',
#                model = 'S710e', loc = htc)
        # Right Up
        #self.mlru = Point.objects.create(lat = 24.975531, lon = 121.327479)
        # Left Up
        #self.mllu = Point.objects.create(lat = 24.975449, lon = 121.327321)
        # Left Down
        #self.mlld = Point.objects.create(lat = 24.975356, lon = 121.327398)
        # Right Down
        #self.mlrd = Point.objects.create(lat = 24.975395, lon = 121.327510)
        self.mlru = Point.objects.create(lat = 11.0, lon = 10.0)
        self.mllu = Point.objects.create(lat = 0.0, lon = 10.0)
        self.mlld = Point.objects.create(lat = 0.3, lon = 0.0)
        self.mlrd = Point.objects.create(lat = 10.0, lon = 0.5)
        self.secru = Section.objects.create(name="RU", lat = self.mlru.lat,
                lon = self.mlru.lon)
        self.seclu = Section.objects.create(name="LU", lat = self.mllu.lat,
                lon = self.mllu.lon)
        self.secld = Section.objects.create(name="LD", lat = self.mlld.lat,
                lon = self.mlld.lon)
        self.secrd = Section.objects.create(name="RD", lat = self.mlrd.lat,
                lon = self.mlrd.lon)
        self.query = "SELECT (abs(lat - %s) + abs(lon - %s)) as \
            distance, ads_section.* FROM ads_section ORDER BY distance ASC \
            LIMIT 10"
        #print Section.objects.raw('ensureIndex({ loc : "2d" }')

    def test_inside_sections(self):
        here = {'lat':1.0, 'lon':0.0}
        wheres = Section.objects.raw(self.query, [here['lat'], here['lon']])
        self.assertEqual(self.secld,wheres[0])

        here = {'lat':6.0, 'lon':4.0}
        wheres = Section.objects.raw(self.query, [here['lat'], here['lon']])
        self.assertEqual(self.secrd,wheres[0])

    def test_outside_sections(self):
        here = {'lat':-1.0, 'lon':0.0}
        wheres = Section.objects.raw(self.query, [here['lat'], here['lon']])
        self.assertEqual(self.secld,wheres[0])

        here = {'lat':100.0, 'lon':200.0}
        wheres = Section.objects.raw(self.query, [here['lat'], here['lon']])
        self.assertEqual(self.secru,wheres[0])
