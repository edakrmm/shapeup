from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def workouts(request):
    
    url = "https://wger.de/api/v2/exercisecategory"

    querystring = {"language": 2}

    headers = {
        'Authorization': "Token a6371866eac053e73c469d09686b6b7fd0b631d8",
        'Content-Type': "application/json"
        }

    print(request.user.is_authenticated)

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    workouts = response['results']
    
    return render(request, 'pages/workouts.html', context={"workouts" : workouts})

    
