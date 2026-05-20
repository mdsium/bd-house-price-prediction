from django.db import models
import json

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"





class HousePrediction(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, help_text="Optional user name")
    email = models.EmailField(blank=True, null=True)
    
    # Input Features
    area_sqft = models.FloatField()
    city = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    floor_level = models.IntegerField()
    total_floors = models.IntegerField()
    building_age = models.IntegerField()
    
    # Amenities (Boolean)
    lift = models.BooleanField(default=False)
    gas_line = models.BooleanField(default=False)
    airco = models.BooleanField(default=False)
    generator = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    prefarea = models.BooleanField(default=False)
    
    # Prediction Result
    predicted_price = models.BigIntegerField()
    formatted_price = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "House Price Prediction"
        verbose_name_plural = "House Price Predictions"

    def __str__(self):
        return f"{self.city} - {self.thana} - ৳{self.formatted_price}"