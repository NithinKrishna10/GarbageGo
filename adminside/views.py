from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from accounts.models import User
import jwt , datetime
from rest_framework.decorators import api_view

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
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


    def get(request,id):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        print(serializer.data)
        return Response(serializer.data)

    # def patch(request,id):
    #     user = User.objects.get(id=id)
    #     serializer = UserSerializer(user,many=False)
    #     return Response(serializer.data)


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