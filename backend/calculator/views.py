from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal

import BigNumber


@api_view(['GET', 'POST'])
def square_root_cap(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


@api_view(['GET', 'POST'])
def module_limits_upload(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
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

        result = BigNumber.sqrt(testnumber)
        return Response(str(result[0]))
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


@api_view(['GET', 'POST'])
def factorial(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")
