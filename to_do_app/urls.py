from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:list_id>/', views.list_page, name='list_page'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
