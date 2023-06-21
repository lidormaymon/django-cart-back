from django.contrib import admin
from .models import Product,Deliveries, Orders


admin.site.register(Deliveries)
admin.site.register(Orders)
admin.site.register(Product)


