from django.contrib import admin
from feature.models import features
# Register your models here.

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('features_heading','features_image','features_price','features_rating_icon1','features_rating_icon2','features_rating_icon3','features_rating_icon4','features_rating_icon5','features_details','features_location','features_days','features_nights')

admin.site.register(features,FeatureAdmin)