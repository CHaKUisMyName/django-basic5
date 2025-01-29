from django.urls import path

from app_users import views

urlpatterns = [
    path('',views.index, name='userIndex'),
    # path('login',views.login),
    path('adduser', views.addUser, name='addUser'),
    path('edituser/<iduser>',views.editUser, name='editUser'),
    path('regis/<id_u>',views.regis,name='userRegis'),
    # path('logout',views.logout),
]