from django.shortcuts import render
from shapeup.models.ongoingchallenges import ChallengesModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def home(request):

    challenges = request.user.challenge.order_by('-id')


    return render(request, 'pages/home.html', context={"challenges":challenges})