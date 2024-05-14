from rest_framework import serializers

from store.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    total_coast = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    def get_total_coast(self, obj):
        coast_products = 0
        items = CartItem.objects.filter(cart=obj.id)
        for item in items:
            coast_products += (item.product.price * item.product_quantity)

        return coast_products

    def get_quantity(self, obj):
        quantity_products = 0
        items = CartItem.objects.filter(cart=obj.id)
        for item in items:
            quantity_products += item.product_quantity

        return quantity_products

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'
