from django.contrib import admin
from django.urls import include, path
from . import views
from .views import profile

urlpatterns = [
	path('', views.register, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', profile, name='profile'),

]
