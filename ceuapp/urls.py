from django.urls import path
from ceuapp import views

urlpatterns = [
    path('',views.index,name='index'),
]
