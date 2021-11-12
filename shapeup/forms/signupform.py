from django.contrib.auth.forms import UserCreationForm
from shapeup.models import CustomUserModel

class signupform(UserCreationForm):
    class Meta:
        model =  CustomUserModel
        abstract = True
        fields = ('email', 'username', 'first_name', 'last_name','password1', 'password2')