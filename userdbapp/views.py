from django.shortcuts import render
from rest_framework.views import APIView
from .models import CDAUsers
from .serializers import CDAUsersSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse, HttpResponse

# Create your views here.
class CDAUsersList(APIView):
    def get(self, request):
        users = CDAUsers.objects.all()
        serializer = CDAUsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CDAUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CDAUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CDAUsers.objects.get(pk=pk)
        except CDAUsers.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CDAUsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CDAUsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)