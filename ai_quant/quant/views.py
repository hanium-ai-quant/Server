from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from quant.serializer import MyTokenObtainPairSerializer, RegisterSerializer, UserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, serializers
from rest_framework.response import Response
from django.contrib import auth

from django.contrib.auth.models import User

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # '/api/token/',
        '/api/signup/',
        # '/api/token/refresh/'
    ]
    return Response(routes)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def login(request):
    try:
        if request.method == 'GET':
            serializer = UserLoginSerializer(data=request.GET)
            print(serializer)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user = auth.authenticate(request, email=email, password=password)
                if user is not None:
                    # 여기에서 로그인 성공 처리
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                else:
                    print("여기")
                    return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                print("여기")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(str(e))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def testEndPoint(request):
#     if request.method == 'GET':
#         data = f"Congratulation {request.user}, your API just responded to GET request"
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         text = request.POST.get('text')
#         data = f'Congratulation your API just responded to POST request with text: {text}'
#         return Response({'response': data}, status=status.HTTP_200_OK)
#     return Response({}, status.HTTP_400_BAD_REQUEST)

# def home(request):
#     return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['nickname'], email=request.POST['email'], password=request.POST['password1'],           
#                 )
#             auth.login(request, user)
#             return redirect('quant')
#     return render(request, 'accounts/signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password) 
        
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home') 
#         else:
#             return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'}) 
#     else:
#         return render(request, 'accounts/login.html')