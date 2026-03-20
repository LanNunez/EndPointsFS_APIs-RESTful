from django.urls import path
from .views import user_list_create, user_detail, random_user

urlpatterns = [
    path('user/', user_list_create, name='user_list_create'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/random/', random_user, name='random_user'),
]
