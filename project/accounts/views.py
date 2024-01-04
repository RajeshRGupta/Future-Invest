from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from .models import OneTimePassword

from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user


# Create your views here.
 
class RegisterUserView(GenericAPIView):
# class RegisterUserView(APIView):
    serializer_class=UserRegisterSerializer

    def post(self,request):
        user_data=request.data
        serializer=self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            send_code_to_user(user['email'])
            #send email function user['email']
            return Response({
                'data':user,
                'message':f"hi {user.first_name} thanks for singing up a passcode has be sent to "
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def get_queryset(self):
    #     return OneTimePassword.objects.all() 

