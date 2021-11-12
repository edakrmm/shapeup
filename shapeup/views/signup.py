from django.shortcuts import render, redirect
from django.contrib import messages
from shapeup.forms import signupform
from django.contrib.auth import authenticate, login


def signup(request):
    form = signupform(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        #messages.success(request, 'Profil başarıyla güncellendi')
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data.get('password1'))
        login(request, user)
        return redirect('home')

    form = signupform()

        
    return render(request, 'pages/signup.html', context={'form': form})