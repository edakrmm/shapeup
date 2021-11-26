from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):

    challenges = request.user.challenge.order_by('-id')
    page = request.GET.get("page")
    paginator = Paginator(challenges,2)

    descriptions = {"abs":"If you’re looking to train your abs, the good news is that there are a huge variety of exercises that will help you achieve that goal",
                    "arms": "f you want to train your arms, you need to take time between training sessions to let the muscles recover and grow",
                    "back": "Back workouts will fix your posture and reduce your risk of injury",
                    "chest": "There are so many chest exercises and workouts to try, from bodyweight staples to twists on dumbbell classics",
                    "legs": "Strong legs do more than look good. Even the simplest daily movements like walking require leg strength",
                    "calves": "Calf exercises serve as a signal of sorts, letting other dudes know that you’re a next-level fitness freak",
                    "shoulders": "The shoulders are delicate and complicated joints that are not especially easy to target"
                    }

    return render(request, 'pages/home.html', context={"challenges": paginator.get_page(page), "descriptions":descriptions})