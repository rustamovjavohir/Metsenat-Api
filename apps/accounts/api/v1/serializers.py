from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.accounts.models import Account


class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(min_length=6, max_length=128, write_only=True)
    password = serializers.CharField(min_length=6, max_length=128, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=128, write_only=True)
    phone = serializers.CharField(min_length=9, max_length=13, write_only=True)
    is_physical_person = serializers.BooleanField(default=False)
    is_legal_entity = serializers.BooleanField(default=False)
    is_student = serializers.BooleanField(default=False)

    class Meta:
        model = Account
        fields = ('id',
                  'full_name',
                  'username',
                  'phone',
                  'password',
                  'password2',
                  'is_physical_person',
                  'is_legal_entity',
                  'is_student',
                  )

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Password did not match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        username = obj.get('username')
        tokens = Account.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('username', 'tokens', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'Username or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        data = {
            'username': user.username,
        }
        return data


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'full_name', 'username', 'phone', 'image')
        extra_kwargs = {
            'image': {'read_only': True}
        }


class AccountSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Account
        fields = (
            'id',
            'full_name',
            'phone',
            'gender',
            'date_login',
            'date_created',

        )
        extra_kwargs = {
            'is_active': {'read_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'full_name', 'phone')


class AccountOwnImageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('image', )