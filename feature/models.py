from distutils.command.upload import upload
from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class features(models.Model):
    features_image = models.FileField(upload_to="img/")
    features_price = models.CharField(max_length=10)
    features_rating_icon1 = models.CharField(max_length=30)
    features_rating_icon2 = models.CharField(max_length=30)
    features_rating_icon3 = models.CharField(max_length=30)
    features_rating_icon4 = models.CharField(max_length=30)
    features_rating_icon5 = models.CharField(max_length=30)
    features_heading = models.CharField(max_length=100)
    features_details = HTMLField()
    features_location = models.CharField(max_length=40)
    features_days = models.CharField(max_length=10)
    features_nights = models.CharField(max_length=10)