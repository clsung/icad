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
                model = 'S710e', loc = sinica)
        self.assertEqual(tagh.model, "S710e")

class SectionTest(TestCase):
    def setUp(self):
#        htc = Point.objects.create(lat = 25.030829, lon = 121.327336)
#        self.tagh = Device.objects.create(imei = '355195000000017',
#                model = 'S710e', loc = htc)
        # Right Up
        self.mlru = Point.objects.create(lat = 24.975531, lon = 121.327479)
        # Left Up
        self.mllu = Point.objects.create(lat = 24.975449, lon = 121.327321)
        # Left Down
        self.mlld = Point.objects.create(lat = 24.975356, lon = 121.327398)
        # Right Down
        self.mlrd = Point.objects.create(lat = 24.975395, lon = 121.327510)
        self.secru = Section.objects.create(name="RU", loc = self.mlru)
        self.seclu = Section.objects.create(name="LU", loc = self.mllu)
        self.secld = Section.objects.create(name="LD", loc = self.mlld)
        self.secrd = Section.objects.create(name="RD", loc = self.mlrd)
        from django.db import connections
        print connections
        db_wrapper = connections['default']
        print db_wrapper.get_collection('section').index_information
        section = db_wrapper.get_collection('section')
        from pymongo import GEO2D
#        index_together = [('loc', GEO2D )]
#        db.eval('db.section.ensureIndex( { loc : "2d" } )')
#        cursor = connections.cursor()
        #cursor.execute('db.section.ensureIndex( { loc : "2d" } )')
#        print Point.objects.ensure_index([( 'loc', "2d")])
        #print Section.objects.raw('ensureIndex({ loc : "2d" }')

    def test_outside_sections(self):
        abc = Point.objects.all()
#        Point.objects.ensuerIndex({ loc : "2d" })
        here = {'lat':24.975048, 'lon':121.327136}
        where = Section.objects.raw_query({'loc' : {'$near' : here}})
        print where
        self.assertEqual(self.secrd,where)

