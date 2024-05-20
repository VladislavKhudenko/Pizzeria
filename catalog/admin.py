from django.contrib import admin

from .models import Pizza, Topping, Order, OrderItem, Jobs

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    # list_view
    list_display = ('price', 'name', 'date', 'text')
    list_filter = ('price','date')
    # detail_view
    fields = [('name', 'price'), 'date', 'text']
    exclude = ['']
class ToppingAdmin(admin.ModelAdmin):
    pass
class OrderAdmin(admin.ModelAdmin):
    pass
class OrderItemAdmin(admin.ModelAdmin):
    pass
class JobsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Jobs, JobsAdmin)
