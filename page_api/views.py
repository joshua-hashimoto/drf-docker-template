from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class PageAPIView(APIView):

    def get(self, request, format=None):
        context = {
            'hello': 'world',
        }
        return Response(data=context, status=status.HTTP_200_OK)
