from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('dashboard', views.accountdata, name='accountdata'),
    path('logout', views.logout, name='logout')
]

