from django.urls import path
from . import views
from .views import api_overview
urlpatterns=[
    path('',views.api_overview,name='api_overview'),
    path('product-list/',views.showall,name='product-list'),
    path('create/',views.createproduct,name='product-create'),
    path('detail/<int:pk>',views.viewproduct,name='product-view'),
    path('update/<int:pk>',views.updateproduct,name='product-update'),
    path('delete/<int:pk>',views.deleteproduct,name='product-delete'),

]
