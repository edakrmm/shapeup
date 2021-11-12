from django.contrib.auth.forms import UserChangeForm
from shapeup.models import CustomUserModel

class UpdateProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUserModel
        fields = ('email','username','first_name', 'last_name', 'avatar')