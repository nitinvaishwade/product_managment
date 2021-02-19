from rest_framework import serializers
from .models import Order, Product, Buyer, Drop

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = '__all__'




# class OrderSerializer(serializers.HyperlinkedModelSerializer):
class OrderSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer()
   
    buyer = BuyerSerializer()
   

    class Meta:
        model = Order
        fields = [ 'product', 'design', 'color', 'buyer']

    def create(self, validated_data):
        product_detail = validated_data.pop('product')
        product, create_obj = Product.objects.get_or_create(name=product_detail['name'], sortno=product_detail['sortno'])
        buyer, buy_created = Buyer.objects.get_or_create(**validated_data.pop('buyer'))
        instance = Order.objects.create(product=product,buyer=buyer, )
        return instance

    