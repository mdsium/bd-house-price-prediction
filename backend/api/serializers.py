from rest_framework import serializers
from .models import ContactMessage

class HousePredictionSerializer(serializers.Serializer):
    area_sqft = serializers.FloatField()
    city = serializers.CharField()
    thana = serializers.CharField()
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    floor_level = serializers.IntegerField()
    total_floors = serializers.IntegerField()
    building_age = serializers.IntegerField()
    lift = serializers.BooleanField()
    gas_line = serializers.BooleanField()
    airco = serializers.BooleanField()
    generator = serializers.BooleanField()
    security = serializers.BooleanField()
    parking = serializers.BooleanField()
    garagepl = serializers.BooleanField()
    road_width_ft = serializers.FloatField()
    distance_main_road_m = serializers.FloatField()
    near_school = serializers.BooleanField()
    near_hospital = serializers.BooleanField()
    near_market = serializers.BooleanField()
    driveway = serializers.BooleanField()
    fullbase = serializers.BooleanField()
    prefarea = serializers.BooleanField()



class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']



class HousePredictionSerializer(serializers.Serializer):
    # Basic Info
    area_sqft = serializers.FloatField()
    city = serializers.CharField()
    thana = serializers.CharField()
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    floor_level = serializers.IntegerField()
    total_floors = serializers.IntegerField()
    building_age = serializers.IntegerField()

    # Amenities
    lift = serializers.BooleanField(default=False)
    gas_line = serializers.BooleanField(default=False)
    airco = serializers.BooleanField(default=False)
    generator = serializers.BooleanField(default=False)
    security = serializers.BooleanField(default=False)
    parking = serializers.BooleanField(default=False)
    prefarea = serializers.BooleanField(default=False)

    # Optional user info
    name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)