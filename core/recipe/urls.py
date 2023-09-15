from django.urls import path
from .views import *
urlpatterns = [
    path('', blank, name='blank'),
    path('recipe/', recipe, name='recipe'),
    path('delete-recipe/<id>', delete_recipe, name='delete_recipe'),
    path('update-recipe/<id>', update_recipe, name='update_recipe'),
    path('register/', register, name='register'),
    path('login/', login_page , name='login'),
    path('logout/', logout_page, name='logout'),
    path('about/', about, name='about'),
    path('userPro/', UserPro, name='UserPro'),
]