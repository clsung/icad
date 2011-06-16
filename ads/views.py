from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from ads.models import *
from django.shortcuts import render_to_response
from django.contrib import auth

def default(request):
    return HttpResponseRedirect("/video")

def serve_video_list(request, format = 'json'):
    mimetype = 'application/javascript'
    data = serializers.serialize(format, Video.objects.all())
    if request.is_ajax():
        if format == 'xml':
            mimetype = 'application/xml'
        return HttpResponse(data,mimetype)
    return HttpResponse(data,mimetype)

def get_video_list(request, lat = None, lon = None, imei = None):
    mimetype = 'application/javascript'
    data = serializers.serialize('json', Device.objects.filter(imei = imei))
    return HttpResponse(data,mimetype)
