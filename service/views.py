import re
import math
import uuid
from django.shortcuts import render
from django.conf import settings
import octopush
from octopush import SMS
from account.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calculate_cost(request):
    BULK_UNIT_COST = settings.BULK_UNIT_COST
    SINGLE_UNIT_COST = settings.SINGLE_UNIT_COST

    leads = request.data['leads']
    job_type = request.data['type']

    pattern = r"[^,]+"
    matches = re.findall(pattern, leads) 

    print(len(matches))

    if job_type == 'SINGLE':
        return Response({'cost': math.floor(1 * SINGLE_UNIT_COST * 100)/100})
    if job_type == 'BULK':
        return Response({'cost': math.floor(len(matches) * BULK_UNIT_COST * 100)/100})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_single_sms(request):
    SINGLE_UNIT_COST = settings.SINGLE_UNIT_COST

    phone_number = request.data['phone_number']
    message = request.data['message']
    sender_name = request.data['sender_name']

    user_profile = Profile.objects.filter(user=request.user)[0]
    user_balance = user_profile.wallet_balance

    print(phone_number, message, sender_name)

    def send_sms(message, phone_number, sender_name) -> bool:
        recipient =[phone_number]
        sender = sender_name
        sms = SMS('landtrash33@gmail.com', 'hnyj2Ll5bApiUcWX1MJqCodF3SmYvuGQ')
        sms.set_sms_text(message)
        sms.set_sms_recipients(recipient)
        sms.set_sms_type(octopush.SMS_PREMIUM)
        sms.set_sms_sender(sender)
        sms.set_sms_request_id(str(uuid.uuid1))
        sent_result = sms.send()
        print(sent_result)

    if user_balance > SINGLE_UNIT_COST:

        sent = send_sms(message, phone_number, sender_name)
        user_profile.wallet_balance = user_balance-SINGLE_UNIT_COST
        user_profile.save()

        if sent:
            return Response(True)
        else:
            return Response(False)
        
    else:
        return Response(status=status.HTTP_402_PAYMENT_REQUIRED)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_bulk_sms(request):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):
    pass