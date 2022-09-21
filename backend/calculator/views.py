from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def square_root(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


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
def add(request):

    if request.method == 'GET':
        return Response("working add")

    elif request.method == 'POST':
        return Response("working add post")


@api_view(['GET', 'POST'])
def subtract(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


@api_view(['GET', 'POST'])
def divide(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


@api_view(['GET', 'POST'])
def multiply(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")


@api_view(['GET', 'POST'])
def factorial(request):

    if request.method == 'GET':
        return Response("working subtract")

    elif request.method == 'POST':
        return Response("working subtract post")
