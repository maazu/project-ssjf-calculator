import re
from unittest import result
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from decimal import getcontext
import numpy as np
from .forms import UploadFileForm
import os
from django.conf import settings
from datetime import datetime
import filetype


@api_view(['GET', 'POST']
          )
def square_root_cap(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


@api_view(['GET', 'POST'])
def step_two(request):
    '''
    Check Mod limit
    '''
    TIMESTAMP = datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%p")
    if request.method == 'POST':
        mod_limit_file = request.FILES['file']

        path = os.path.join(settings.MEDIA_ROOT,
                            str(TIMESTAMP) + '-' + mod_limit_file.name)

        with open(path, 'w') as infile:
            str_repr = mod_limit_file.read().decode()
            infile.write(str_repr)

        

        return Response("working subtract post")


@api_view(['GET', 'POST'])
def step_four(request):
    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


'''

Additional Calculator Feature Enpoints

'''


@api_view(['GET', 'POST'])
def square_root(request):
    if request.method == 'POST':
        data = request.data
        testnumber = data['testNumber']
        number = data['number2']
        n = Decimal(number)
        getcontext().prec = 10000
        result = n.sqrt()

        return Response(str(result))
    else:
        return Response("working add")


@api_view(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        data = request.data
        testnumber = data['testNumber']
        number = data['number2']
        result = testnumber + number
        return Response(str(result))
    else:
        return Response("working add")


@api_view(['GET', 'POST'])
def subtract(request):
    if request.method == 'POST':
        data = request.data
        testnumber = data['testNumber']
        number = data['number2']
        result = testnumber - number
        return Response(str(result))
    else:
        return Response("please send the post request payload")


@api_view(['GET', 'POST'])
def divide(request):
    if request.method == 'POST':
        data = request.data
        testnumber = data['testNumber']
        number = data['number2']
        result = testnumber / number
        return Response(str(result))
    else:
        return Response("please send the post request payload")


@api_view(['GET', 'POST'])
def multiply(request):
    if request.method == 'POST':
        data = request.data
        testnumber = data['testNumber']
        number = data['number2']
        result = testnumber * number
        return Response(str(result))
    else:
        return Response("please send the post request payload")


def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x


@api_view(['GET', 'POST'])
def factorial(request):
    if request.method == 'POST':
        try:
            data = request.data
            testnumber = data['testNumber']
            number = data['number2']

            res = sum(int(digit)
                      for digit in str(factorial(number)))

            return Response(str(res))

        except Exception as e:
            print(e)
            return Response('Factorial Error :' + str(e))

    else:
        return Response("please send the post request payload")
