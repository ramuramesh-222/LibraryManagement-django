from django.urls import path
from .views import *

urlpatterns = [
    path('customers/',customerlist),
    path('customers/add/',customeradd),
    path('customer/delete/<int:id>/',deletecustomer,name = 'customer_delete'),
    path('customer/upadte/<int:id>/',updatecustomer,name = 'customer_update'),
    path('orders/',orderslist),
    path('add/orders/',ordersadd),
    path('delete/order/<int:id>',ordersdelete,name='order_delete'),
    path('update/order/<int:id>',ordersupdate,name='order_update'),





]   
