from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    # ex:  https://www.optabot.ai/
    path('', views.index, name='index'),
    # ex:  https://www.optabot.ai/home/
    path('home/', views.home, name='home'),
    # ex:  https://www.optabot.ai/login/
    path('login/', views.login, name='login'),
    # ex:  https://www.optabot.ai/register/
    path('register/', views.register, name='register'),
]