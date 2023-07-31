from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import PublisherOrReadOnly
from .models import Product
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class ProductGetView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        paginator = PageNumberPagination()
        result = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = ProductSerializer(result, many=True)
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


class ProductUpdateView(APIView):
    permission_classes = [IsAuthenticated, PublisherOrReadOnly]

    def put(self, request, pk):
        instance = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Product Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
