from django.urls import path
from .views import home, product_detail, sub_product_detail

urlpatterns = [
    path('', home, name='home'),  # Main Page
    path('product/<int:product_id>/', product_detail, name='product_detail'),  # Product Detail Page
    path('sub-product/<int:image_id>/', sub_product_detail, name='sub_product_detail'),  # Sub-Product Detail Page
]
