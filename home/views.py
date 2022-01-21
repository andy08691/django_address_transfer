from django.shortcuts import render, HttpResponse
from home.geoProcessing import geoProcessing
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'home/home.html')
  
@csrf_exempt
def get_geo_location(request):
    print('get_geo_location', request.body.decode('utf-8'))
    # body = request.body.decode('utf-8')
    # body_unicode = request.body.decode('utf-8')
    body = json.loads(request.body)
    address = body['address']
    result  = geoProcessing(address)
    print('result', result, type(result))
    return HttpResponse(json.dumps(result)) 
  