from django.urls import path
from home import views

urlpatterns = [
    path('add/', views.add_Book, name='add_Book'),
    path('display/', views.display_Book, name='display_Book'),
    path('edit/<int:id>/', views.edit_Book, name='edit_Book'),
    path('delete/<int:id>/', views.delete_Book, name='delete_Book'),
]
