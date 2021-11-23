from django.urls import path
from shapeup.views import muscles, home, workouts, signup, logoutview, updateprofile, workouts,workoutdetails
from django.contrib.auth import views

urlpatterns = [
    path('', home, name='home'),
    path('muscles/', muscles, name='muscles'),
    path('workouts/',workouts, name='workouts'),
    path('workoutdetails/<slug:slug>',workoutdetails, name='workoutdetails'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutview, name='logoutview'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('login/', views.LoginView.as_view(template_name="pages/login.html"), name='login'), #djangonun auth view ları class based view lar. Class based viewları view olarak kullanmak için .as_view kullanıyoruz.
]
