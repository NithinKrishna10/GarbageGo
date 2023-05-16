from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt , datetime
from rest_framework import permissions, status
from rest_framework.decorators import api_view
# Create your views here.
# class RegisterView(APIView):
#     def post(self, request):
#         print(request.data)
#         # serializer = UserSerializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         data = request.data
        
#         email = data['email']
#         emaiexit = User.objects.filter(email=email)
#         print("dhisfklertyiwocnvm,x.asdfhkluj :" ,emaiexit)
#         if emaiexit:
#             errors = "alredy exits"
#             print(errors)
#             return Response(errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = UserSerializer(data=data)
#         print(serializer)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         user = serializer.create(serializer.validated_data)
#         user = UserSerializer(user)

#         return Response(user.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.data)
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        print('iam in the register')
        if User.objects.filter(email=email).exists():
            # errors = {'email': ['Email already exists.']}
            return Response({"status":"Email already exists"}, status=status.HTTP_409_CONFLICT)

        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = serializer.save()
            print(user,'isdfjakiasdfjkl;')
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        print("hai Login View")
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'status':'Please provide the mentioned details'})
            user = User.objects.filter(email=email).first()
 
        
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                Response({'status':'Password is incorrect'})
            if user is not None:
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
                    'phone': user.phone,
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')
 
                print(token,"toooooooooooken")
                return Response({'status' : "Success",'payload' : payload ,'user_jwt': token,'user':userdetails})
        except:
            if User.DoesNotExist:
                return Response("Email or Password is Wrong") 


class UserView(APIView):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'

    def get(self, request):
        print(request.data,'hjdfhjkasdfhjkasdfhjkasdfhjksdf')
        # token = request.data['body']
        # print(token)
        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET'])   
def verify_token(request):
    # token  = request['body']
    token = request.headers.get('Authorization')
    print("###################################",token,'############################################')
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    print(decoded)
    print(decoded.get('id'),'Yes iam back////.......')
    id = decoded.get('id')
    user = User.objects.get(id=id)
    print(user)
    # serializer = UserSerializer(user)
    serializer = UserSerializer(user,many=False)

    if user:
        userdetails ={
                    'name': user.name,
                    'email' : user.email,
                    'phone': user.phone,
                }
       
        return Response({'user':userdetails})
    else:
        return Response({'status' : 'Token Invalid'})


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

