from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScrapCategorySerializer, ScrapSerializer
from scrap.models import ScrapCategory, Scrap

class ScrapCategoryAPIView(APIView):
    def get(self, request):
        categories = ScrapCategory.objects.all()
        serializer = ScrapCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScrapCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapAPIView(APIView):
    def get(self, request):
        scraps = Scrap.objects.all()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = ScrapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapCategoryDetailAPIView(APIView):
    def get_category(self, pk):
        try:
            return ScrapCategory.objects.get(pk=pk)
        except ScrapCategory.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ScrapCategorySerializer(category)
        return Response(serializer.data)

    def patch(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ScrapCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ScrapDetailAPIView(APIView):
    def get_scrap(self, pk):
        try:
            return Scrap.objects.get(pk=pk)
        except Scrap.DoesNotExist:
            return None

    def get(self, request, pk):
        scrap = self.get_scrap(pk)
        if not scrap:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ScrapSerializer(scrap)
        return Response(serializer.data)

    def patch(self, request, pk):
        scrap = self.get_scrap(pk)
        if not scrap:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ScrapSerializer(scrap, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        scrap = self.get_scrap(pk)
        if not scrap:
            return Response(status=status.HTTP_404_NOT_FOUND)
        scrap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
