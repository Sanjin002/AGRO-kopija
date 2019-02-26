from rest_framework import serializers
from .models import Crop, Category

class CropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crop
        fields = ('id','url', 'name', 'description', 'uses','growing_period','further_info','Physiology','category','temp_abs_min','temp_abs_max','temp_opt_min','temp_opt_max','rf_abs_min','rf_abs_max','rf_opt_min','rf_opt_max','crop_cycle')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','url','name')