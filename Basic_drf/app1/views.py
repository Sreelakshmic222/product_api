from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List': '/product-list',
        'Detail': '/product-detail/<int:id>',
        'Update': '/product-update/<int:id>',
        'Create': '/product-create',
        'Delete': '/product-delete/<int:id>'
    }
    return Response(api_urls)


@api_view(['Get'])
def showall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#Create
@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Single View
@api_view(['Get'])
def viewproduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

#Update
@api_view(['Post'])
def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#delete
@api_view(['Delete'])
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Deleted Successfully")


