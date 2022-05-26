from django.urls import path

from django_filters.views import FilterView

from .models import Product

from .views import *

urlpatterns = [
    path('lists/', ListProductView.as_view()),
    path('lists/', FilterView.as_view(model=Product), name='product-list'),
    path('<int:pk>/', RetrieveProductView.as_view()),
    path('create/', CreateProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),
]
