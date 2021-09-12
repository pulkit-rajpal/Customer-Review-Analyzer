from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('login/', include(login.urls))
    path("",views.login,name='login'),
    path("login/signIn/",views.signIn,name="signIn"),
    #path("",views.signOut,name="signOut"),
    path("login/register/",views.register,name='register'),
    path("logout", views.logout_req, name= "logout"),
    #path("login/forget_pass", views.forget_pass, name="forget_pass"),


]
