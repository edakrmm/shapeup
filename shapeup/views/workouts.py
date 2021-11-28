from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger('workouts_displayed')

@login_required(login_url='login')
def workouts(request):        

    if request.user.is_authenticated:
        logger.info('workouts_displayed:' + request.user.username)

    return render(request, 'pages/workouts.html', context={})

    
