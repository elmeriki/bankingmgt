from django.urls import path,include
from . import views

urlpatterns = [
    path('createuserbankaccount', views.createuserbankaccount, name='createuserbankaccount'),
    path('createdeposit', views.createdeposit, name='createdeposit'),
    path('createuseraccountinfo', views.createuseraccountinfo, name='createuseraccountinfo'),
    path('fetchbalance', views.fetchbalance, name='fetchbalance'),
    path('fetchstatement', views.fetchstatement, name='fetchstatement'),
    path('fetchuser', views.fetchuser, name='fetchuser'),
]

