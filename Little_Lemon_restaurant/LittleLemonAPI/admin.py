from django.contrib import admin
from LittleLemonAPI.models import *

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)