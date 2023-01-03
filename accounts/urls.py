from django.urls import path
from django.contrib.auth import views as auth_views
from book_store_app import views
from .views import UserCreate

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html",
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", UserCreate.as_view(), name="register"),
]