from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import requests

# 📌 Criar e Listar usuários
@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':  # Listar todos os usuários
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  # Criar um novo usuário
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 📌 Buscar, Atualizar e Deletar um usuário por ID
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Buscar usuário por ID
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':  # Atualizar usuário
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':  # Deletar usuário
        user.delete()
        return Response({'message': 'Usuário deletado'}, status=status.HTTP_204_NO_CONTENT)

# 📌 Criar um usuário aleatório a partir da API RandomUser.me
@api_view(['POST'])
def random_user(request):
    try:
        response = requests.get('https://randomuser.me/api/', timeout=5)
        data = response.json()
        random_user = data['results'][0]

        new_user = {
            'user_nickname': random_user['login']['username'],
            'user_name': f"{random_user['name']['first']} {random_user['name']['last']}",
            'user_email': random_user['email'],
            'user_age': random_user['dob']['age'],
            'user_birthdate': random_user['dob']['date'].split('T')[0],
        }

        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)