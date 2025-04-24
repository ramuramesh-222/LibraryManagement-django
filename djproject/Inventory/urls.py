from django.urls import path
from .views import *

urlpatterns = [
    #path('products/add/',productsadd),
    #path('products/',allproducts),
    #path('products/delete/<int:id>/',deleteproduct,name = 'product_delete'),
    #path('products/update/<int:id>/',updateproduct,name = 'product_update'),
    path('products/add/',productaddview.as_view()),
    path('products/',listprodectview.as_view()),
    path('products/delete/<int:id>/',prodectdeleteview.as_view(),name = 'product_delete'),
    path('products/update/<int:id>/',productdeleteview.as_view(),name = 'product_update'),


]
