from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import PostSerializer, CategorySerializer, TagSerializer, PostSerializerr
from blog.models import Post, Tag, Category
from .permissions import IsTokenVerified


class PostCategoryView(APIView):
    permission_classes = [IsTokenVerified]
    def get(self, request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)


class PostTagView(APIView):
    permission_classes = [IsTokenVerified]
    def get(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)

        return Response(serializer.data)


class PostView(APIView):
    permission_classes = [IsTokenVerified]
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializerr(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [IsTokenVerified]
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
