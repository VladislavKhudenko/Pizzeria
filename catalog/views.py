from django.shortcuts import render
from .models import Pizza, Topping, Order, OrderItem, Jobs
from django.views import generic



# Create your views here.
def index(request):

    num_pizza = Pizza.objects.all()
    num_topping = Topping.objects.all()
    num_order = Order.objects.all()
    num_orderitem = OrderItem.objects.all()
    num_jobs = Jobs.objects.all()
    
    return render(request,'index.html',context={'num_pizza':num_pizza,
        'num_topping':num_topping,
        'num_order':num_order,
        'num_orderitem':num_orderitem,
        'num_jobs':num_jobs},)


class PizzaListView(generic.ListView):
    model = Pizza
class PizzaDetailView(generic.DetailView):
    model = Pizza
class JobsDetailView(generic.DetailView):
    model = Jobs