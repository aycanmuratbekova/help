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


class DonationAPIView(generics.ListAPIView):

    serializer_class = DonationSerializer

    def get(self, category_id, **kwargs):
        queryset = Donation.objects.filter(id=category_id)
        serializer = DonationSerializer(queryset, many=True)
        return Response(serializer.data)






