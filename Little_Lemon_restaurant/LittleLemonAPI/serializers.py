from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id','username','groups','email']
        fields='__all__'
        
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','featured','category']
        extra_kwargs = {
            'price': {'min_value': 2}
        }
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug','title']
        
class CartSerializer(serializers.ModelSerializer):

    #price = serializers.SerializerMethodField(method_name = 'calculate_price')
    class Meta:
        model = Cart
        fields = ['user','menuitem','quantity','unit_price','price']
    """  
    def calculate_price(self,product:Cart):
        p=MenuItem.objects.get(title=product.menuitem.title)
        product.price = product.quantity * p.price
        product.save()
        return product.quantity * p.price
    """
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =  '__all__'