

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
 
    path('',views.index,name='index' ),
    path('about_us/',views.about_us,name='about_us'),
    path('register/',views.register,name='register'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('predict/',views.manipulate,name='predict'),
    path('logout/',views.logout_view,name='logout'),
    path('add_data/',views.add_data,name='add_data'),
    path('ask_here/',views.ask_here,name='ask_here'),
]
