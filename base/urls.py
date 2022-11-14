from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<int:pk>/', views.userProfile, name="user-profile"),
    path('create-room', views.createRoom, name="create-room"),
    path('edit-room/<int:pk>/', views.updateRoom, name="edit-room"),
    path('delete-room/<int:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<int:pk>/', views.deleteMesaage, name="delete-message"),
    path('update-user', views.updateUser, name="update-user")

]
