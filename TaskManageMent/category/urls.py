from django.urls import path 
from . import views
urlpatterns = [
    path('',views.category_list, name = 'category_list'),
    path('add/',views.add_category, name = 'add_category'),
    path('category/<int:category_id>/', views.category_list, name='category_list'),
]
