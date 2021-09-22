from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:genre_slug>/', views.genre_list, name='genre_list'),
]
