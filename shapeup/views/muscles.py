from django.shortcuts import render
import os
import requests

def muscles(request):
    
    url = "https://wger.de/api/v2/muscle"
    main_url = "https://wger.de/"

    querystring = {"language": 2}

    headers = {
        'Authorization': "Token a6371866eac053e73c469d09686b6b7fd0b631d8",
        'Content-Type': "application/json"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    muscles = response['results']
    
    return render(request, 'pages/muscles.html', context={"muscles" : muscles})

    
