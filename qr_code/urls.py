
from django.urls import path
from qr_code import views

app_name = 'products'

urlpatterns = [
path('qr-code/', views.qr_code_view, name='qr_code'),
]

