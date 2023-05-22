from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
def login_view(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user=user)
    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token
    })
    
    
@api_view(['GET'])
def get_user_data(request):
    user = request.user
    print(request)
    print(user)
    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
        })
    return Response({'error': "not authenticated"}, status='400')

@api_view(['POST'])
def register_view(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
        })

    