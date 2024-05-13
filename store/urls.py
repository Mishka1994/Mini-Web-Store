from django.urls import path

from store.apps import StoreConfig
from store.views import CategoryCreateView, SubcategoryCreateView, ProductCreateView, ProductListView, \
    ProductRetrieveView

app_name = StoreConfig.name

urlpatterns = [

    path('category/create/', CategoryCreateView.as_view(), name='category-create'),

    path('subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory-create'),

    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/list/', ProductListView.as_view(), name='product-list'),
    path('product/retrieve/<int:pk>/', ProductRetrieveView.as_view(), name='product-retrieve')

]

