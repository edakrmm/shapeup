from django.shortcuts import render, redirect
from django.contrib import messages
from shapeup.forms import SignupForm
from django.contrib.auth import authenticate, login


def signup(request):
    form = SignupForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
       
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data.get('password1'))
        login(request, user)
        return redirect('home')

    form = SignupForm()

        
    return render(request, 'pages/signup.html', context={'form': form})