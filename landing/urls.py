from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('View_student_details/<str:username>',views.view_student_details,name='View_student_details'),
    path('loggedin', views.loggedin, name='loggedin'),
]
