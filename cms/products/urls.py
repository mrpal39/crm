from django.urls import path

from cms.products.views import *

app_name = "products"
urlpatterns = [
    path("update/", get_product_name_modile, name="update"),
]
