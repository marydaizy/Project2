from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Officer, Farmer, Season, Report
from rest_framework import viewsets
from farm.serializers import UserSerializer, GroupSerializer, OfficerSerializer, FarmerSerializer, SeasonSerializer, ReportSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class OfficerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows officer to be viewed or edited.
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farmer to be viewed or edited.
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows season to be viewed or edited.
    """
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows report to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
