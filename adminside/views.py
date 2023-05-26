from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer,UserCreateSerializer
from rest_framework import status
from accounts.models import User
import jwt , datetime
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
# Create your views here.
class RegisterView(APIView):
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        if user.is_superuser is False:
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')


        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'
    @extend_schema(responses=UserSerializer)
    def get(self, request):
        print(request)
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
class UserApi(APIView):

    @extend_schema(responses=UserSerializer)
    def get(request,id):
        print("had")
        user = User.objects.all()
        print(user)
        serializer = UserSerializer(user,many=True)
        print(serializer.data)
        return Response(serializer.data)



    def patch(request,id):
        user = User.objects.get(id=id)
        user.full_name = request.data["username"]
        user.email = request.data["email"]
        user.save()
        return Response("User Updated")


    def delete(request,id):
        user = User.objects.get(id=id)
        user.delete()
        return Response("User deleted")
    

@api_view(['GET'])
@extend_schema(responses=UserSerializer)
def userlist(request):
    user = User.objects.all()
    serializer = UserCreateSerializer(user,many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['PATCH'])
def block_user(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return Response({'status': 'blocked'})

@api_view(['PATCH'])
def unblock_user(request, id):
    user = User.objects.get(id=id)
    print(user)
    user.is_active = True
    user.save()
    return Response({'status': 'blocked'})




#  ============================= Scrap ==========================================

from services.models import Category

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


from rest_framework import serializers
from services.models import Scrap, Category,Waste

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ScrapSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Scrap
        fields = ['id', 'name', 'category', 'description', 'weight', 'price', 'image']
        read_only_fields = ['id']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(id=category_data['id'])
        scrap = Scrap.objects.create(category=category, **validated_data)
        return scrap

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(id=category_data['id'])
        instance.name = validated_data.get('name', instance.name)
        instance.category = category
        instance.description = validated_data.get('description', instance.description)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


@api_view(['POST'])
def create_scrap(request):
    serializer = ScrapSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ############################################################
@api_view(['GET'])
def list_scraps(request):
    scraps = Scrap.objects.all()
    serializer = ScrapSerializer(scraps, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_scrap(request, pk):
    try:
        scrap = Scrap.objects.get(pk=pk)
    except Scrap.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ScrapSerializer(scrap, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_scrap(request, pk):
    try:
        scrap = Scrap.objects.get(pk=pk)
    except Scrap.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    scrap.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


   
