from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from .models import User
import jwt


class IsTokenVerified(BasePermission):

    def has_permission(self, request, view):

        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        id = decoded.get('id')
        user = User.objects.get(id=id)
        if user:
            # userdetails = UserSerializer(user,many=False)

            return True
        else:
            return False