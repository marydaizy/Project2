
from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True)
    sub_county = models.CharField(max_length=50, null=True)
    farmer = models.ForeignKey('Farmer', on_delete= models.CASCADE, null=True)
    class Meta:
        
        ordering = ('district',)

    def __str__(self):
        return self.district+" : "+self.parish+" : "+self.sub_county

class Officer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    login_id =models.CharField(max_length=50, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    district = models.CharField(max_length=50, null=True)
    subcounty = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=15, null=True)
    


    def __str__(self):
        return self.username

class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=30,null=True)
    subcounty = models.CharField(max_length=30,null=True)
    parish = models.CharField(max_length=30,null=True)
    village = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    marriage_status =models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=15,null=True)
    photo = models.FileField(null=True)
    community_status = models.TextField(null=True)
    instructor_possibility = models.BooleanField(null=True)
    farm_area = models.CharField(max_length=50,null=True)
    crop_type = models.CharField(max_length=20, null=True)
    past_harvest = models.TextField(null=True)
    officers = models.ForeignKey('Officer', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.username

class Season(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    season = models.CharField(max_length=100, null=True)
    area = models.IntegerField(null=True)
    harvest = models.IntegerField(null=True)
    farmers = models.ForeignKey('Farmer', on_delete= models.CASCADE, null=True)


    def __str__(self):
        return self.username

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True)
    season = models.CharField(max_length=30,null=True)
    area = models.CharField(max_length=30,null=True)
    rice_type = models.CharField(max_length=30,null=True)
    sowing_date = models.DateTimeField(null=True)
    sowing_type = models.CharField(max_length=10,null=True)
    planting_type = models.CharField(max_length=20, null=True)
    levelling =models.CharField(max_length=20, null=True)
    ridge = models.CharField(max_length=10,null=True)
    whatercourse_state = models.CharField(max_length=15,null=True)
    fertilizer = models.BooleanField(null=True)
    fertilizre1_type = models.CharField(max_length=20, null=True)
    fertilizer1_amount = models.IntegerField(null=True)
    fertilizre2_type = models.CharField(max_length=20, null=True)
    fertilizer2_amount = models.IntegerField(null=True)
    weed_condition = models.CharField(max_length=50,null=True)
    total_weed_times = models.IntegerField(null=True)
    harvest_date = models.DateTimeField(null=True)
    harvest_amount = models.IntegerField(null=True)
    note = models.TextField(null=True)
    photo1 = models.FileField(null=True)
    photo2 = models.FileField(null=True)
    photo3 = models.FileField(null=True)
    photo4 = models.FileField(null=True)
    farmer = models.ForeignKey('Farmer', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.username



