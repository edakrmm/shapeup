from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url="login")
def changepassword(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, "Password updated successfully")
            return redirect('changepassword.html')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/change-password.html', context={"form":form})