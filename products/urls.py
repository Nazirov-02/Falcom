
from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
path('products',views.product_list, name='list'),
path('detail/<int:pk>/',views.product_detail, name='detail'),
path('comment/<int:pk>',views.comment, name='comment'),
path('product_search', views.search,name='search'),
]
