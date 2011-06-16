from django.db import models

class Point(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

class Device(models.Model):
    last_seen = models.DateTimeField(auto_now_add=True, null=True)
    imei = models.CharField( max_length = 15)
    model = models.CharField( max_length = 10 )
    phone_number = models.CharField( max_length = 15)
    email = models.EmailField()
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()

    def __unicode__(self):
        return '%s(%s)' % self.model, self.imei

class Video(models.Model):
    create_on = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField( max_length = 255 )
    tags = models.TextField()
    url = models.CharField( max_length = 255)
    thumbnail = models.CharField( max_length = 255)

class Section(models.Model):
    name = models.CharField( max_length = 255)
    tags = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __unicode__(self):
        return "%s(%f,%f)" % (self.name, self.lat, self.lon)
