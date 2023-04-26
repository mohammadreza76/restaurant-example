from django.urls import path
from LittleLemonAPI import views

urlpatterns =[
    path('menu-items',views.MenuItemsViewList.as_view()),
    path('menu-items/<int:pk>',views.MenuItemView.as_view()),
    path('groups/manager/users',views.show_add_manager),
    path('groups/manager/users/<int:pk>',views.delete_from_manager_or_delivery_crew), #delete from manager
    path('groups/delivery-crew/users',views.show_add_deliverycrew),
    path('groups/delivery-crew/users/<int:pk>',views.delete_from_manager_or_delivery_crew), #delete from delivery_crew    
    path('cart/menu-items',views.show_add_delete_items_cart),#show-add-delete cart
    path('orders',views.create_retrieve_order),
    path('orders/<int:pk>',views.change_delete_get_order_item),
    
]
