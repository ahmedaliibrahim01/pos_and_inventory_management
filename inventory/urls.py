from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Item işlemleri
    #path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),

    # AJAX destekli arama
    #path('stock/search/', views.stock_search, name='stock_search'),

    # ✅ New Stock sayfası
    path('new-stock/', views.new_stock, name='new_stock'),
]
