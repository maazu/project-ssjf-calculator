from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def add(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        return Response('working')

    elif request.method == 'POST':
        return Response('data added', status=status.HTTP_201_CREATED)
