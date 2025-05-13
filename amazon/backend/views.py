from django.shortcuts import render

# Create your views here.
 from rest_framework import viewsets
 from .models import cliente
 from .serializers import clienteSerializer

 class clienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer