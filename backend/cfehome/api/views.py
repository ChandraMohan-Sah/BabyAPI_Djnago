from django.shortcuts import render
from django.http import JsonResponse

import json
# Design Our First API

def api_home(request, *args, **kwargs):
    # request -> HttpRequest From -> Django
    # request.body
    print(request.GET) #url query params 
    #print(request.POST)

    body = request.body  # byte string of JSON data (not Exactly JSON data)
    #to convert this string into Actual JSON We have to import JSON

    
    data = {}
    try: 
        data =  json.loads(body)
    except:
        pass
    print(data.keys())

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse({
        "message" : "Hi there , this is your Djnago API Response!!"
    })


