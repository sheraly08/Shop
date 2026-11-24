from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.decorators import  api_view

# Create your views here.
@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategorySerializer(categories, many=True).data

    return Response(data=list_)

@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(category, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    list_ = ProductSerializer(products, many=True).data

    return Response(data=list_)

@api_view(http_method_names=['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(reviews, many=True).data

    return Response(data=list_)

@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)
