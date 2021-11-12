from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from shapeup.forms import UpdateProfileForm
from shapeup.models.users import CustomUserModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def updateprofile(request):
    user = get_object_or_404(CustomUserModel, username = request.user)
    form = UpdateProfileForm(request.POST or None, files=request.FILES or None,instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile has been updated successfully')
        
    return render(request, 'pages/updateprofile.html', context={'form': form})