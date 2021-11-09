from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UpdateUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class PasswordChangeSerializer(ModelSerializer):
    new_password = serializers.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ["password"]

    def update(self):
        """
        Validate that the old_password field is correct.
        """
        if not self.user.check_password(self.old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        try:
            validate_password(self.new_password)
        except:
            raise ValidationError("Password Validation Failed")
        
        self.user.set_password(self.new_password)
        self.user.save()
        return self.user