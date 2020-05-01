from django.urls import path
from store import views


urlpatterns = [

    #path('', views.home, name='home'),
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_itme/', views.updateItem, name='update_itme'),

]
