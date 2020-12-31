from django.urls import path
from shop import views


urlpatterns = [
    path('', views.home, name="go_to_home_page"),
    path('product', views.product, name="go_to_product_page"),
    path('<slug:category_slug>', views.home,
         name='products_by_category'),
]
