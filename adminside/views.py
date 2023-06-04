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
from rest_framework.exceptions import APIException


class RegisterView(APIView):
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class LoginView(APIView):
   
 
    
    def post(self, request):
        print("hai Login View")
        try:
            email = request.data['email']
            password = request.data['password']
            print(password)
        except:
            return Response({'status':'Please provide the mentioned details'})
        user = User.objects.filter(email=email).first()
        print(user.password)
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                Response({'status':'Password is incorrect'})
            if not user.is_admin:
                Response({'status':'User not admin'})
                
            if user is not None:
                # user = LoginSerializer(user)
                print('kkkkkkkkkkkk')
                payload = {
                        'id': user.id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                        'iat': datetime.datetime.utcnow(),
                        'name' : user.name
                    }
                userdetails ={
                    'name': user.name,
                    'email' : user.email,
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')
 
                print(token,"toooooooooooken")
                return Response({'status' : "Success",'payload' : payload ,'admin_jwt': token,'admin':userdetails})
        except:
            if User.DoesNotExist:
                return Response("Email or Password is Wrong") 
            

class UserView(APIView):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'

    @extend_schema(responses=UserSerializer)
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired!')

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed('User not found!')

        serializer = UserSerializer(user)
        return Response(serializer.data)



  
@api_view(['GET'])
@extend_schema(responses=UserSerializer)   
def verify_token(request):
    try:
        token = request.headers.get('Authorization')

        # print("###################################",token,'############################################')
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        # print(decoded)
        # print(decoded.get('id'),'Yes iam back////.......')
        id = decoded.get('id')
        user = User.objects.get(id=id)
     
       

        if user:
            # userdetails = UserSerializer(user,many=False)
            userdetails ={
                        'id':user.id,
                        'name': user.name,
                        'email' : user.email,
                        
                    }
        
            return Response({'admin':userdetails})
        else:
            return Response({'status' : 'Token Invalid'})
    except APIException as e:
        return Response(
                {
                    'verify_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successful'
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



