from django.http import JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView

from .models import Product
from .serializers import ProductSerializer, UserSerializer
from .serializers import User


class ProductHome(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = [ProductSerializer(instance).data for instance in products]
        return Response({'data': data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)


class UserGet(APIView):
    def get(self, request):
        user = get_object_or_404(User, id=1)
        data = UserSerializer(user).data
        return Response(data)


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        data = serializer.validated_data
        print(data)
        serializer.save()


class ProductListAPIVeiw(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

