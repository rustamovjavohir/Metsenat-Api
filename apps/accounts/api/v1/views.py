from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from apps.accounts.models import Account
from .permissions import IsOwnUserOrReadOnly
from .serializers import RegisterSerializer, LoginSerializer, AccountSerializer, AccountOwnImageUpdateSerializer


class AccountRegisterAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/register/
    serializer_class = RegisterSerializer

    # user create
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': True, 'message': 'You should login'},
                        status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Credentials is not valid'}, status=status.HTTP_400_BAD_REQUEST)


class AccountListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/account/login/profiles/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)
    pagination_class = None


class MyAccountAPIView(generics.RetrieveUpdateAPIView):
    # http://127.0.0.1:8000/account/login/{phone}/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)
    lookup_field = 'phone'


class AccountOwnImageUpdateView(generics.RetrieveUpdateAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/image-update/<id>/
    serializer_class = AccountOwnImageUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsAuthenticated, IsOwnUserOrReadOnly)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'query does not match'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Credentials is invalid'}, status=status.HTTP_400_BAD_REQUEST)