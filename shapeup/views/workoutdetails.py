from django.shortcuts import  render
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shapeup.models import ChallengesModel
challenges = []


@login_required(login_url='login')
def workoutdetails(request,slug):
    
    if slug=='arms':
        querystring = {"language": 2,"category":8}
        bot=0
        top=3
    elif slug=='legs':
        querystring = {"language": 2,"category":9}
        bot=3
        top=6
    elif slug=='abs':
        querystring = {"language": 2,"category":10}
        bot=6
        top=9
    elif slug=='chest':
        querystring = {"language": 2,"category":11}
        bot=9
        top=12
    elif slug=='back':
        querystring = {"language": 2,"category":12}
        bot=12
        top=15
    elif slug=='shoulders':
        querystring = {"language": 2,"category":13}
        bot=15
        top=18
    elif slug=='calves':
        querystring = {"language": 2,"category":14}
        bot=18
        top=21

    headers = {
        'Authorization': "Token a6371866eac053e73c469d09686b6b7fd0b631d8",
        'Content-Type': "application/json"
        }
    
    response = requests.get("https://wger.de/api/v2/exercise", headers=headers, params=querystring)
    response = response.json()
    workout = response['results']

    response = requests.get("https://wger.de/api/v2/exerciseimage", headers=headers, params=querystring)
    response = response.json()
    img = response['results'][bot:top]

    if ChallengesModel.objects.filter(challenges=slug, challenger=request.user).exists():
        check = False
    else:
        check = True
    
    if 'start' in request.POST:
        if check==True:
            challenge = ChallengesModel()
            challenge.challenges = slug
            challenge.challenger = request.user
            challenge.save()
            messages.success(request, "You have started this challenge")
            check=False
            

    
    elif 'stop' in request.POST:
        if ChallengesModel.objects.filter(challenges=slug, challenger=request.user).exists():
            ChallengesModel.objects.get(challenges=slug, challenger=request.user).delete()
            messages.warning(request, "You have quited this challenge")
            check = True
           
    
    return render(request, 'pages/workoutdetails.html', context={"workout" : workout, "img":img, "check":check, "slug":slug})

