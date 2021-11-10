from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from userAuth.serializers import RegisterUserSerializer, UpdateUserProfileSerializer, PasswordChangeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterUser(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


class BlackListTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = RefreshToken(request.data["refresh_token"])
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except TokenError:
            return Response("Invalid Token", status=status.HTTP_400_BAD_REQUEST)


class UpdateUserProfileView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserProfileSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if self.request.user.id != self.kwargs["pk"]:
            raise ValidationError(
                {"error": "You dont have permission to peform this action"})
        return super().update(request, *args, **kwargs)


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            if not self.request.user.check_password(serializer.validated_data.get("old_password")):
                raise ValidationError(
                    self.error_messages['password_incorrect'],
                    code='password_incorrect',
                )
            validate_password(serializer.validated_data.get("new_password"))
            self.request.user.set_password(serializer.validated_data.get("new_password"))
            self.request.user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)