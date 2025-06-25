from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('items/', views.item_list, name='items'),
    path('stock/', views.stock, name='stock'),
    path('pos/', views.pos, name='pos'),

    # Item işlemleri
    path('items/update/<int:item_id>/', views.update_item, name='update_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),

    # AJAX destekli arama
    path('stock/search/', views.stock_search, name='stock_search'),

    # ✅ New Stock sayfası
    path('new-stock/', views.new_stock, name='new_stock'),
]
