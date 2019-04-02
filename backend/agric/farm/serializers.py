from django.contrib.auth.models import User, Group
from .models import Officer, Farmer, Season, Report
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class OfficerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Officer
        fields = ('username', 'login_id' , 'email', 'district', 'subcounty', 'telephone')

class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ('username', 'parish', 'village', 'gender', 'age', 'marriage_status', 'language', 'telephone', 'photo', 'community_status', 'instructor_possibility', 'farm_area', 'crop_type', 'past_harvest')

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('username', 'season', 'area', 'harvest')

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('username', 'season', 'area', 'rice_type', 'sowing_date', 'sowing_type', 'planting_type', 'levelling', 'ridge', 'whatercourse_state', 'fertilizer', 'fertilizre1_type', 'fertilizer1_amount', 'fertilizer2_amount', 'weed_condition', 'total_weed_times', 'harvest_date', 'harvest_amount', 'note', 'photo1', 'photo2', 'photo3', 'photo4', 'user')