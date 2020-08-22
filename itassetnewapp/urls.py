from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('al', views.asset_list, name='asset_list'),
    path('ae', views.asset_entry, name='asset_entry'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout')
]
