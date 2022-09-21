from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
