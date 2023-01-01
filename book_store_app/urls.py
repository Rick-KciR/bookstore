from django.urls import path
from book_store_app import views

urlpatterns = [
    path("", views.home_page, name="url_home_page"),
]