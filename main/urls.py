from django.urls import path
from . import views



urlpatterns = [
    path("", views.index,name="index"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin,name="signin"),
    path("logout",views.log_out,name="logout"),
    path("settings", views.settings,name="settings")
    
]
