from django.shortcuts import render
import requests


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
   
 
    return render(request, 'pages/workoutdetails.html', context={"workout" : workout, "img":img})



# from django.shortcuts import render
# import requests

# def workoutnames(request):

#     url = "https://wger.de/api/v2/exercise"

#     name_arms = []
#     name_legs = []
#     name_abs = []
#     name_chest = []
#     name_back = []
#     name_shoulders = []
#     name_calves = []

#     description_arms = []
#     description_legs = []
#     description_abs = []
#     description_chest = []
#     description_back = []
#     description_shoulders = []
#     description_calves = []

#     for i in range(8,15):
        
#         querystring = {"category": i, "language":2}

#         headers = {
#             'Authorization': "Token a6371866eac053e73c469d09686b6b7fd0b631d8",
#             'Content-Type': "application/json"
#             }

#         response = requests.request("GET", url, headers=headers, params=querystring)
#         response = response.json()
#         response = response['results']
#         for j in range(len(response)):
#             if i==8:
#                 name_arms.append(response[j]['name'])
#             if i==9:
#                 name_legs.append(response[j]['name'])
#             if i==10:
#                 name_abs.append(response[j]['name'])
#             if i==11:
#                 name_chest.append(response[j]['name'])
#             if i==12:
#                 name_back.append(response[j]['name'])
#             if i==13:
#                 name_shoulders.append(response[j]['name'])
#             if i==14:
#                 name_calves.append(response[j]['name'])
#         for j in range(len(response)):
#             if i==8:
#                 description_arms.append(response[j]['description'])
#             if i==9:
#                 description_legs.append(response[j]['description'])
#             if i==10:
#                 description_abs.append(response[j]['description'])
#             if i==11:
#                 description_chest.append(response[j]['description'])
#             if i==12:
#                 description_back.append(response[j]['description'])
#             if i==13:
#                 description_shoulders.append(response[j]['description'])
#             if i==14:
#                 description_calves.append(response[j]['description'])
    
#     print(description_legs)