from django.urls import path
from .views import ServiceOrderView, UserOrderListView
from apps.orders.views import order_post, get_user_orders

urlpatterns = [
    path('order-post/', order_post, name='order-post.html'),
    path('form/<int:pk>/', ServiceOrderView.as_view(), name='order-form'),
    path('myorders/', get_user_orders, name='user-orders'),
]
