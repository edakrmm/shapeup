from django.shortcuts import render

def workouts(request):        
    return render(request, 'pages/workouts.html', context={})

    
