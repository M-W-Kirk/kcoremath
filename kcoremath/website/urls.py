from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
   path('', views.home, name='home'),
   path('add.html', views.add, name='add'),
   path('subtract.html', views.subtract, name="subtract"),
   path('multipy.html', views.multiply, name='multiply'),
   path('divide.html', views.divide, name='divide'),
]