from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
   path('', views.login_user, name='login2'),
   path('home.html', views.home, name='home'),
   path('add.html', views.add, name='add'),
   path('subtract.html', views.subtract, name="subtract"),
   path('multipy.html', views.multiply, name='multiply'),
   path('divide.html', views.divide, name='divide'),
   path('sign-in/', views.login_user, name='login2'),
   path('sign-out/', views.logout_user, name='logout'),
   path('sign-in/', views.redirect_signin, name='redirect_signin'),
]