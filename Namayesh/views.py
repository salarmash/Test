from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Product
from rest_framework import status


class ProductGetView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPostView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["publisher"] = request.user
            serializer.save()
            return Response({'Message': "Product Added"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

