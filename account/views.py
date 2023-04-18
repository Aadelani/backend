from django.shortcuts import render

from ast import Return
from django.http import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from coinbase_commerce import Client    
from .models import User
from .serializers import *  
from .models import Payment


from django.conf import settings
from django.core.mail import send_mail
# from services import utils

# Create your views here.

@api_view(["GET"])
def home(request):
    endpoint = [
        "home/"
    ]

    return Response(endpoint)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data
# LOGIN USER GOES HERE
class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# GET PROFILE
@api_view(["GET"])
def user_profile(request):
    userProfile = Profile.objects.get(user=request.user)

    serializers = ProfileSerializer(userProfile, many=False)

    print(request.user)

    return Response(serializers.data)

# REGISTER USER GOES HERE
@api_view(["POST"])
def register_user(request):
    data = request.data

    user = User.objects.create(
        username=data["username"],
        first_name= data["username"],
        email=data["email"],
        password=make_password(data["password"])
    )

    serializers = UserSerializerWithToken(user, many=False)

    return Response(serializers.data)

@api_view(["POST"])
def wallet_deposit(request):
    amount = int(request.data['amount'])

    print(amount)

    API_KEY = "f1a6e1e9-fe67-4938-9bf0-4acae136f8ed"
    client = Client(api_key=API_KEY)
    
    checkout_info = {
        "name": 'XXXSimple',
        "description": 'Wallet deposit at xxxsimple.',
        "pricing_type": 'fixed_price',
        "local_price": {
            "amount": str(amount),
            "currency": "USD"
        },
        "requested_info": []
    }
    checkout = client.checkout.create(**checkout_info)
    checkout = dict(checkout)
    
    id_ = checkout["id"]
    checkout = client.checkout.retrieve(id_)
    #building out the coinbase deposit url

    url = "https://commerce.coinbase.com/checkout/" + id_
    # print(url)

    payment = Payment.objects.create(user=request.user, amount=amount)
    payment.save()

    return Response({'url':url})