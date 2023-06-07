from pickup.models import PickupRequest
from adminside.serializers import OrderSerializer
from orders.models import Order
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, LoginSerializer, LoginDetailsSerializer, AddressSerializer, CitySerializer, DistrictSerializer, AddressPostSerializer, PickupSerializer
from .models import User, Address, City, District
import jwt
import datetime
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import APIException


class RegisterView(APIView):
    @extend_schema(
        responses=UserSerializer,
        request=UserSerializer,)
    @extend_schema(responses=UserSerializer)
    def post(self, request):
        try:
            data = request.data
            email = data.get('email')
            if User.objects.filter(email=email).exists():
                # errors = {'email': ['Email already exists.']}
                return Response({"status": "Email already exists"}, status=status.HTTP_409_CONFLICT)

            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = serializer.save()
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response(
                {
                    'register_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):

    @extend_schema(
        responses=LoginSerializer,
        # Assuming the request schema is the same as the response schema
        request=LoginSerializer,
    )
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'status': 'Please provide the mentioned details'})
        user = User.objects.filter(email=email).first()
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                Response({'status': 'Password is incorrect'})
            if user is not None:
                # user = LoginSerializer(user)
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
                    'iat': datetime.datetime.utcnow(),
                    'name': user.name
                }
                userdetails = {
                    'name': user.name,
                    'email': user.email,
                    'phone': user.phone,
                }

                token = jwt.encode(payload, 'secret', algorithm='HS256')

                return Response({'status': "Success", 'payload': payload, 'user_jwt': token, 'user': userdetails})
        except:
            if User.DoesNotExist:
                return Response("Email or Password is Wrong")


class UserView(APIView):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'

    @extend_schema(responses=UserSerializer)
    def get(self, request):
        token = request.data['body']
        try:
            payload = jwt.decode(token, self.JWT_SECRET,
                                 algorithms=[self.JWT_ALGORITHM])
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

        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        id = decoded.get('id')
        user = User.objects.get(id=id)

        if user:
            # userdetails = UserSerializer(user,many=False)
            userdetails = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
            }

            return Response({'user': userdetails})
        else:
            return Response({'status': 'Token Invalid'})
    except APIException as e:
        return Response(
            {
                'verify_errors': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    def post(self, request):
        try:
            response = Response()
            response.delete_cookie('jwt')
            response.data = {
                'message': 'success'
            }

        except APIException as e:
            return Response(
                {
                    'order_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


# for(i=0,i<10,i++)
# for i in range(10):
class AddressListAPIView(APIView):

    def get(self, request, id):
        try:
            userId = id  # Assuming you are using authentication and the user ID is available in the request
            addresses = Address.objects.filter(user=userId)
            serializer = AddressSerializer(addresses, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {
                    'Addres_error': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class AddressPostAPIView(APIView):

    def post(self, request):
        try:
            serializer = AddressPostSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response(
                {
                    'Address_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST

            )


class DistrictListAPIView(APIView):
    def get(self, request):
        try:

            districts = District.objects.all()
            serializer = DistrictSerializer(districts, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'district': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityListAPIView(APIView):
    def get(self, request):
        try:
            cities = City.objects.all()
            serializer = CitySerializer(cities, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'city except': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            orders = Order.objects.filter(customer=user)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'OrderList except': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class CustomerPickupRequestAPIView(APIView):
    def get(self, request, customer_id):
        try:
            pickup_requests = PickupRequest.objects.filter(
                customer_id=customer_id)
            serializer = PickupSerializer(pickup_requests, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
