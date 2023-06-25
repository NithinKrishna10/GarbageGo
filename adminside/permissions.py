from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from accounts.models import User
import jwt
class TokenVerificationPermission(BasePermission):
    """
    Custom permission class to verify the token for authentication.
    """

    def has_permission(self, request, view):
        # Perform token verification here
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]

        # Verify the token using TokenAuthentication
        token_auth = TokenAuthentication()
        try:
            user, _ = token_auth.authenticate_credentials(token)
            return True
        except AuthenticationFailed:
            return False


class IsTokenVerified(BasePermission):

    def has_permission(self, request, view):

        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        print(token)
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        id = decoded.get('id')
        user = User.objects.get(id=id)
        if user.is_admin:
            # userdetails = UserSerializer(user,many=False)

            return True
        else:
            return False