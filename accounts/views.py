from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer ,LoginSerializer,LoginDetailsSerializer,AddressSerializer,CitySerializer,DistrictSerializer,AddressPostSerializer
from .models import User,Address,City,District
import jwt , datetime
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema 


class RegisterView(APIView):
    @extend_schema(responses=UserSerializer)
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
   
 
    @extend_schema(
    responses=LoginSerializer,
    request=LoginSerializer,  # Assuming the request schema is the same as the response schema
)
    def post(self, request):
        print("hai Login View")
        try:
            email = request.data['email']
            password = request.data['password']
            print(password)
        except:
            return Response({'status':'Please provide the mentioned details'})
        user = User.objects.filter(email=email).first()
        
        try:
            user = User.objects.get(email=email)
            print(user)
            if not user.check_password(password):
                Response({'status':'Password is incorrect'})
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
    @extend_schema(responses=UserSerializer)
    def get(self, request):
        print(request.data,'hjdfhjkasdfhjkasdfhjkasdfhjksdf')
        token = request.data['body']
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
@extend_schema(responses=UserSerializer)   
def verify_token(request):
    try:
        token = request.headers.get('Authorization')

        print("###################################",token,'############################################')
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        print(decoded)
        print(decoded.get('id'),'Yes iam back////.......')
        id = decoded.get('id')
        user = User.objects.get(id=id)
        print(user)
        # serializer = UserSerializer(user)
       

        if user:
            # userdetails = UserSerializer(user,many=False)
            userdetails ={
                        'name': user.name,
                        'email' : user.email,
                        'phone': user.phone,
                    }
        
            return Response({'user':userdetails})
        else:
            return Response({'status' : 'Token Invalid'})
    except:
        pass


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

# for(i=0,i<10,i++)
# for i in range(10):
#     print("Hai")
class AddressListAPIView(APIView):
    def get(self, request,id):
        print(request,id)
        userId = id  # Assuming you are using authentication and the user ID is available in the request
        print(userId)
        addresses = Address.objects.filter(user=userId)
        print(addresses)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)


class AddressPostAPIView(APIView):
    print("kpodfij")
    def post(self, request):
        print(request.data)
        serializer = AddressPostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors,"errooooooooooooooooooooooor")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





class DistrictListAPIView(APIView):
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityListAPIView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




