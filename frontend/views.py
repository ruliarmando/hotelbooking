import urllib
import urllib2
from django.shortcuts import render
from django.http import Http404
from django.conf import settings

def index(request):
    return render(request, 'frontend/index.html', {'message': 'Hello Django!'})

def search_hotel(request):
    base_url = 'https://api.master18.tiket.com/search/hotel?'
    fields = {
        'q': 'Kepulauan Riau',
        'startdate': '2014-03-04',
        'night': 1,
        'enddate': '2014-03-05',
        'room': 1,
        'adult': 2,
        'token': settings.TIKET_COM_TOKEN,
        'output': 'json'
    }
    query_url = base_url + urllib.urlencode(fields)
    response = urllib2.urlopen(query_url)
    return render(request, 'frontend/search.html', {'html': response.read()})
