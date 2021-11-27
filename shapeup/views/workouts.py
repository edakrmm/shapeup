from django.shortcuts import render
import logging

logger = logging.getLogger('workouts_displayed')

def workouts(request):        

    if request.user.is_authenticated:
        logger.info('workouts_displayed:' + request.user.username)

    return render(request, 'pages/workouts.html', context={})

    
