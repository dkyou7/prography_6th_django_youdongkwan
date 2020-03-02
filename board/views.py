from django.shortcuts import render
from rest_framework import generics

from .models import Board
from .serializer import BoardSerializer

from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    queryset = Board.objects.all()
    serializer_class = BoardSerializer

