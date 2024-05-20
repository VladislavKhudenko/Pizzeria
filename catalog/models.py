from django.db import models
from django.urls import reverse

# Create your models here.
# Создание класса пицца:
class Pizza(models.Model):

    # наименование пиццы
    name = models.CharField(max_length=100, help_text = "Введите наименование пиццы")
    # десятичное число фиксированнйо длины(m_d - максимальное количество цифр, d_p - количество десятичных знаков)
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text = "Укажите цену BYN")
    text = models.TextField(max_length=1000, help_text = "Дайте описание пиццы", null = True , blank = True)
    date = models.DateTimeField(null = True , blank = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """
        Returns the url to access a particular pizza instance.
        """
        return reverse('pizza-detail', args=[str(self.id)])
    

# Создание модели для представления ингредиентов:
class Topping(models.Model):
    name = models.CharField(max_length=50, help_text = "Введите наименование дополнительного ингредиента")

    def __str__(self):
        return self.name

# Создание модели для представления заказов:
class Order(models.Model):
    # имя клиента
    customer_name = models.CharField(max_length=100)
    # связка заказа с пиццами (отношение многие ко многим)
    pizzas = models.ManyToManyField(Pizza, through='OrderItem')

    def __str__(self):
        return f"Order for {self.customer_name}"

# Промежуточная модель для связи заказов с пиццами:
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text = "Имя клиента")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.pizza.name} in order {self.order.id}"
    
class Jobs(models.Model):

    # наименование вакансии
    name = models.CharField(max_length=100, help_text = "Введите наименование вакансии")
    # Зарплата
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text = "Укажите зарплату в BYN", null = True , blank = True)
    text = models.TextField(max_length=1000, help_text = "Описание вакансии", null = True , blank = True)
