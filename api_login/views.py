from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api_login.serializers import UserSerializer
import project_dogger.services.custom_response as custom_response


class CreateUserAPI:
    @staticmethod
    @permission_classes([permissions.AllowAny])
    @api_view(['POST'])
    def create_user(request):
        if request.method == 'POST':
            request_data = request.data
            user_data = {
                'username': request_data.get("username", None),
                'password': request_data.get("password", None),
                'first_name': request_data.get("name", None),
                'last_name': request_data.get("last_name", None),
                'phone': request_data.get("phone", None),
                'email': request_data.get("email", None),
                'profile_id': request_data.get("profile_id", None),
            }

            print(user_data)
            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                estado = UserSerializer().create_user_custom(user_data=user_data)
                return custom_response.response_ok(data=str(estado))

            return custom_response.response_error(data=str(serializer.errors))


class LogoutView(APIView):
    # permission_classes = (AllowAny,)

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print('logout method')
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return custom_response.response_ok()
        except Exception as e:

            return custom_response.response_error(data=str(e))
