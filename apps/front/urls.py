from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('list/',views.list,name='list'),
]