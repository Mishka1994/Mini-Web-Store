from django.urls import path

from store.apps import StoreConfig
from store.views.cart import CartCreateView, CartItemCreateView, CartRetrieveView
from store.views.category import CategoryCreateView
from store.views.product import ProductCreateView, ProductListView, ProductRetrieveView, ProductFilterView
from store.views.subcategory import SubcategoryCreateView

app_name = StoreConfig.name

urlpatterns = [
    # urls for Category
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    # urls for Subcategory
    path('subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory-create'),
    # urls for Product
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/list/', ProductListView.as_view(), name='product-list'),
    path('product/filter_list/', ProductFilterView.as_view(), name='product-filterlist'),
    path('product/retrieve/<int:pk>/', ProductRetrieveView.as_view(), name='product-retrieve'),
    # urls for Cart
    path('cart/create/', CartCreateView.as_view(), name='cart-create'),
    path('cart/retrieve/<int:pk>/', CartRetrieveView.as_view(), name='cart-retrieve'),

    # urls for CartItem
    path('cartitem/create/', CartItemCreateView.as_view(), name='cartitem-create'),

]

