from django.urls import path
from .views import register_user, login_user, logout_user, manage_profile

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', manage_profile, name='manage_profile'),
]

