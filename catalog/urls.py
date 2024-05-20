from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name ='index'),
    re_path(r'^pizza/$', PizzaListView.as_view(), name='pizza'),
    re_path(r'^pizza/(?P<pk>\d+)$', PizzaDetailView.as_view(), name='pizza-detail'),
    path('jobs', JobsDetailView.as_view(), name='jobs'),
]