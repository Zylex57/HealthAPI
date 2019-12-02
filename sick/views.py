from django.shortcuts import render
from rest_framework import generics
from sick.serializers import SickDetailSerializer, SickListSerializer
from sick.models import Sick


# Create your views here.

class SickCreateView(generics.CreateAPIView):
    serializer_class = SickDetailSerializer


class SickListView(generics.ListAPIView):
    serializer_class = SickListSerializer
    queryset = Sick.objects.all()


class SickDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SickDetailSerializer
    queryset = Sick.objects.all()
