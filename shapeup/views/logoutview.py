from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutview(request):
    logout(request)
    return redirect('login')