from django import template
import requests

register = template.Library()

@register.simple_tag
def muscle_list():
    
    url = "https://wger.de/api/v2/exercisecategory"

    querystring = {"language": 2}

    headers = {
        'Authorization': "Token a6371866eac053e73c469d09686b6b7fd0b631d8",
        'Content-Type': "application/json"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    response = response['results']
    musclelist = []

    for resp in response:
        for key, value in resp.items():
            if key=='name':
                musclelist.append(value)
    print(musclelist)     
           
    return musclelist