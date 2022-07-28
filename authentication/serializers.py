from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering users"""

    # Defining our fields
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = PhoneNumberField()
    date_of_birth = serializers.DateField()
    address = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True) # Do not return the password when registering


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'address', 'password']


    # Validating fields before registering the user
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists() # Check if user with this email already exists in the database

        if email_exists:
            raise serializers.ValidationError('Email already exists, please login')
        else:
            return attrs


    # When all fields validated, create the user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)