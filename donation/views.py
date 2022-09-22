# import APIView as APIView
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, DonationSerializer
from .models import Donation, Category
from rest_framework.decorators import api_view
from rest_framework import viewsets


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()









