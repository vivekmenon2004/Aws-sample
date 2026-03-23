from django.urls import path
from . import views

urlpatterns = [
    # Phones
    path('', views.phone_list, name='phone_list'),
    path('phone/<int:pk>/', views.phone_detail, name='phone_detail'),
    path('phone/add/', views.phone_add, name='phone_add'),
    path('phone/<int:pk>/edit/', views.phone_edit, name='phone_edit'),
    path('phone/<int:pk>/delete/', views.phone_delete, name='phone_delete'),
    # Brands
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/add/', views.brand_add, name='brand_add'),
]
