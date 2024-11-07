from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from telegram.service import send_message


# Create your views here.


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def telegram(request):

    data = request.data

    print(data)

    chat_id = data['message']['chat']['id']

    send_message(chat_id, "Hello There")

    return HttpResponse('OK!')
