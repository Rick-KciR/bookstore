from django.urls import path
from book_store_app import views

urlpatterns = [
    path("", views.index, name="url_index"),
    path("about/", views.about, name="url_about"),
    path("form/", views.create_book),
    path("listagem/", views.book_list, name="url_booklist"),
    path("delete/<int:pk>/", views.delete, name="url_delete"),
    path("update/<int:pk>/", views.update, name="url_update"),
    path("novo/", views.create_book, name="url_new"),
]