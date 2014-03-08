import urllib
import urllib2
import json

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'frontend/index.html', {'message': 'Hello Django!'})

def search_hotel(request):
    fields = {
        'q': 'Riau',
        'startdate': '2014-03-20',
        'night': 1,
        'enddate': '2014-03-21',
        'room': 1,
        'adult': 2,
        'token': settings.TIKET_COM_TOKEN,
        'output': 'json'
    }
    query_url = settings.TIKET_COM_API_URL + urllib.urlencode(fields)
    response = urllib2.urlopen(query_url)
    the_json = json.loads(response.read())
    json_formatted = json.dumps(the_json, indent=4, separators=(',', ': '), sort_keys=True)
    return HttpResponse('<pre>' + json_formatted + '</pre>')
    #return render(request, 'frontend/search.html', {'html': response.read()})

