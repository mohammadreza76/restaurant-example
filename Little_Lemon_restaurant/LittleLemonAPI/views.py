from .models import *
from rest_framework import generics,status
from rest_framework.decorators import api_view,permission_classes,action
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissions,IsAuthenticated
from django.contrib.auth.models import User,Group
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import random,datetime
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class ResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 300

class MenuItemsViewList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = ResultsSetPagination
    
    
class MenuItemView(generics.RetrieveUpdateDestroyAPIView,
                   generics.CreateAPIView):
    
    permission_classes = [DjangoModelPermissions]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
#show manager list and add manager   
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def show_add_manager(request):
    if request.method == 'GET':
        managers = User.objects.all().filter(groups__name='Manager')
        serializer = UserSerializer(managers,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        id =request.data.get('id')
        user = User.objects.get(id=id)
        user.groups.set([1])       
        user.save()
        return Response(status= status.HTTP_201_CREATED)

#delete manager  
@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_from_manager_or_delivery_crew(request,pk):
    user  = get_object_or_404(User,id=pk)
    user.groups.set([])       
    user.save()
    return Response(status= status.HTTP_200_OK)

#show delivery crew  list and add delivery crew   
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def show_add_deliverycrew(request):
    if request.method == 'GET':
        delivery_crew  = User.objects.all().filter(groups__name='Delivery crew')
        serializer = UserSerializer(delivery_crew,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        id =request.data.get('id')
        user = User.objects.get(id=id)
        user.groups.set([2])       
        user.save()
        return Response(status= status.HTTP_201_CREATED)
    
   
#show-add-delete-items-cart
@api_view(['POST','GET','DELETE'])
@action(methods=["DELETE"], detail =False, )
@permission_classes([IsAuthenticated])
def show_add_delete_items_cart(request):  
    if request.method == 'POST':
        item = MenuItem.objects.get(id =request.data['menuitem'])
        
        request.data._mutable = True
        request.data['unit_price'] = item.price
        request.data['price'] = item.price * int(request.data['quantity'])
        request.data._mutable = False
        
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        carts = Cart.objects.all().filter(user = request.user)
        serializer = CartSerializer(carts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        carts = Cart.objects.all().filter(user = request.user)
        carts.delete()
        return Response(status=status.HTTP_200_OK)
        
    
@api_view(['GET','POST'])    
@action(methods=["DELETE"], detail =False, )
@permission_classes([IsAuthenticated])
def create_retrieve_order(request):
    user = User.objects.get(username = request.user)

    
    if request.method == 'GET':
        if user.groups.filter(name='Manager').exists():
            orders = Order.objects.all()           
            paginator = ResultsSetPagination()
            context = paginator.paginate_queryset(orders, request)
            serializer = OrderSerializer(context,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif user.groups.filter(name= 'Delivery crew').exists():
            orders = Order.objects.all().filter(delivery_crew=user)
            serializer = OrderSerializer(orders,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            orders = Order.objects.all().filter(user=user)
            serializer = OrderSerializer(orders,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    else:
        carts = Cart.objects.all().filter(user=user)
        delivery_crew_assign = random.choice(User.objects.all().filter(groups__name='Delivery crew'))
        order = Order.objects.create(user = user, delivery_crew=delivery_crew_assign,date= datetime.datetime.now() )
        order.save()
        total_price=0

        for cart in carts:
            order_item = OrderItem.objects.create(order=order,menuitem=cart.menuitem,quantity=cart.quantity,
                                     unit_price=cart.unit_price,price=cart.price)
            order_item.save()
           
            total_price += cart.price
  
        
        order.total = total_price
        order.save()
        carts.delete()
        return Response(status=status.HTTP_200_OK)
            
          
@api_view(['PUT','GET','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def change_delete_get_order_item(request,pk):
    order_user = get_object_or_404(Order,id=pk)
    
    if request.method == 'GET':        
        order_items = OrderItem.objects.all().filter(order=order_user)
        if (len(order_items))>1:
            serializer = OrderItemSerializer(order_items,many=True)
        else:
            serializer = OrderItemSerializer(order_items)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if request.user in User.objects.all().filter(groups__name='Manager'):
            order_user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    elif request.method == 'PATCH' or request.method == 'PUT':

        if request.user == order_user.delivery_crew:

            order_user.status = request.data['status']
            order_user.save()
            return Response(status=status.HTTP_200_OK)
        
        elif request.user in User.objects.all().filter(groups__name='Manager'):

            if request.data['status'] != None:
                order_user.status = request.data['status']
            if request.data['delivery_crew'] != None:
                delivery = User.objects.get(id = request.data['delivery_crew'])
                order_user.delivery_crew = delivery
            
            order_user.save()
            
            return Response(status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    
    
    
    
