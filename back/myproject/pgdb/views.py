from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Feature, Like
from .serializers import UserSerializer, FeatureSerializer, LikeSerializer

# Create your views here.

class FeatureList(APIView):

  def get(self, request):
    feature = Feature.objects.all()
