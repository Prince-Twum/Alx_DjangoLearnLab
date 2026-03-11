from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/', views.edit_book, name='edit_book'),
    path('delete-book/', views.delete_book, name='delete_book'),
]