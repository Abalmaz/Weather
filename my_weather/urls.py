from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='my_weather/login.html'), name='login'),
]
